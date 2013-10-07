#!/usr/bin/python

import urllib, pycurl, os
from tweet import Geocode_Search
from random import randint
import operator


def downloadFile(url, fileName):
    fp = open(fileName, "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()

def getGoogleSpeechURL(phrase):
    googleTranslateURL = "http://translate.google.com/translate_tts?tl=en&"
    parameters = {'q': phrase}
    data = urllib.urlencode(parameters)
    googleTranslateURL = "%s%s" % (googleTranslateURL,data)
    return googleTranslateURL

def speakSpeechFromText(phrase, fileName):
    googleSpeechURL = getGoogleSpeechURL(phrase)
    print googleSpeechURL
    downloadFile(googleSpeechURL,fileName)
    #os.system("afplay tts.mp3")


def getMashedText(results):
	combined_string = ''
	for x in results:
		combined_string += x.text
	#break down string to list
	combined_string_list = list(combined_string)
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	alphabet_count = {}
	#resetting the count list
	for j in alphabet:
		alphabet_count[j] = 0
	#creat count dictionary
	for y in combined_string_list:
		for z in alphabet:
			z = unicode(z)
			if z is y:
				alphabet_count[z] += 1
	
		
	
	#summerize all counts
	total = 0
	for l in alphabet:
		total += alphabet_count[l]
		if total is 0:
			total = 1	
		
	for m in alphabet:
		temp = alphabet_count[m]
		alphabet_count[m] = temp * 100 / total
	#Generate Mashed text
	mashedtext = ''
	for n in range(0,99):
		slots = {}
		for p in alphabet:
			slots[p] = alphabet_count[p] * randint(1,100)
			if slots[p] is 0:
				temp = randint(1,100)
				if temp <= 10:
					slots[p] = 1
			slots[','] = (len(results)+1) * randint(0,100) / 5
		
		
		mashedtext += max(slots.iteritems(),key=operator.itemgetter(1))[0]	
			
	
	return mashedtext
				









