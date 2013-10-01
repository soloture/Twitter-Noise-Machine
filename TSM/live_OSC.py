import OSC
import time, random

live_client = OSC.OSCClient()
live_client.connect(('127.0.0.1',9000))


live_tweets = OSC.OSCMessage()
live_tweets.setAddress("/live/tempo")
live_tweets.append(100.0)

live_client.send(live_tweets)

live_words=OSC.OSCMessage()
live_words.setAddress("/live/device")
live_words.append(0)
live_words.append(1)
live_words.append(30)
#live_words.append(5)
live_words.append(0.1)

live_client.send(live_words)

live_words1=OSC.OSCMessage()
live_words1.setAddress("/live/device")
live_words1.append(2)
live_words1.append(0)
live_words1.append(5)
live_words1.append(15)

live_client.send(live_words1)