import OSC
import time, random

client = OSC.OSCClient()
client.connect(('127.0.0.1',57120))

tweets = OSC.OSCMessage()
tweets.setAddress("/tweets")
tweets.append(1)

words = OSC.OSCMessage()
words.setAddress("/words")
words.append(200)

client.send(tweets)
client.send(words)