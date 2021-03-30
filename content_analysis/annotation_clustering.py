import pandas as pd
import generic_clustering as gc

limit = 10

df = pd.read_csv("final_annotations.csv").head(limit)

df = gc.encode_text(df, text_column="messages")

df.to_csv("annotation_encodings.csv")

df, centroids = gc.cluster(df, n_clusters=7)

print(df.groupby(["label"]).size())

gc.print_centroids(df, centroids, text_column="messages")

print(gc.get_df_for_label(df, 0)["messages"])
