import OSC
import time, random

client = OSC.OSCClient()
client.connect(('127.0.0.1',57120))

tweets = OSC.OSCMessage()
tweets.setAddress("/tweets")
tweets.append(0.5)

words = OSC.OSCMessage()
words.setAddress("/words")
words.append(10)

client.send(tweets)
client.send(words)