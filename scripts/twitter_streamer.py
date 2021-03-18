import tweepy


class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        with open("fetched_tweets.txt", "a") as tf:
            tf.write(data)
        return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print(status)  # Currently Erroring out with 401


auth = tweepy.OAuthHandler(
    "",  # token
    "",  # secret
)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()


while True:
    try:
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        myStream.filter(track=["hi"], stall_warnings=True)

    except KeyboardInterrupt:
        myStream.disconnect()
        break
