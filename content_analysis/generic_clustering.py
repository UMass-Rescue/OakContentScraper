import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.cluster import KMeans

model = SentenceTransformer("bert-base-nli-stsb-mean-tokens")


def encode_text(df, text_column="text", output_column="text_vecs"):
    df[output_column] = model.encode(df[text_column].tolist()).tolist()
    return df


def cos_distance(a, b):
    a_dot_b = np.dot(a, b)
    mag_a_mag_b = np.linalg.norm(a) * np.linalg.norm(b)
    return a_dot_b / mag_a_mag_b


def find_closest_word_from_vec(df, vec, vector_column="text_vecs", text_column="text"):
    cur_max = cos_distance(df[vector_column][0], vec)
    cur_word = df[text_column][0]

    for index, row in df.iterrows():
        dist = cos_distance(row[vector_column], vec)
        if dist > cur_max:
            cur_max = dist
            cur_word = row[text_column]

    return cur_word, cur_max


def calc_distances(df, target_row):
    text_vecs = df.text_vecs.tolist()
    distances = list()
    for i in range(0, len(text_vecs)):
        dist = cos_distance(text_vecs[i], text_vecs[target_row])
        distances.append(dist)

    df["distances"] = distances
    return df


def _find_similar_strings(df_a, query_vec, threshold, target_column, output_column):
    body_vecs = df_a[target_column].tolist()
    distances = list()
    for i in range(0, len(body_vecs)):
        dist = cos_distance(body_vecs[i], query_vec)
        distances.append(dist)

    df_a[output_column] = distances
    df_a = df_a.sort_values(by=[output_column], ascending=False)
    df_a = df_a[df_a[output_column] > threshold]
    return df_a


def find_similar_strings(
    df,
    search_string,
    similarity_threshold=0.5,
    text_column="text",
    target_column="text_vecs",
    output_column="similarity",
):
    vectorized_input = model.encode([search_string])[0]
    df_closest_matches = _find_similar_strings(
        df.copy(), vectorized_input, similarity_threshold, target_column, output_column
    )
    return df_closest_matches[[text_column, "similarity"]]


def cluster(
    df,
    vector_column="text_vecs",
    n_clusters=20,
    random_state=0,
    output_label_col="label",
):
    all_body_vecs = np.asarray(df[vector_column].tolist())
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(all_body_vecs)
    cluster_labels = kmeans.predict(all_body_vecs)
    df[output_label_col] = cluster_labels
    centroids = kmeans.cluster_centers_
    return df, centroids


def print_centroids(df, centroids, text_column="text"):
    for index, centroid in enumerate(centroids):
        print(
            f"Index: {index} Centroid label: {find_closest_word_from_vec(df,centroid, text_column=text_column)}"
        )


def get_df_for_label(df, label_number, label_column="label"):
    return df[df[label_column] == label_number]


if __name__ == "__main__":
    """
    Sample usage
    """
    data = {"text": ["hi", "hey", "what's up", "how's it going"]}
    df = pd.DataFrame(data)

    df = encode_text(df)

    df, centroids = cluster(df, n_clusters=4)

    print_centroids(df, centroids)
