from soundgenerator import downloadFile, getGoogleSpeechURL, speakSpeechFromText, getMashedText
from tweet import Geocode_Search
import time

last_id = 0
fileName = 'tts'


while 1:
	results = Geocode_Search(34.1844709,-118.131809,'0.5km',last_id)
	print len(results[0])
	speakSpeechFromText('aeae,ab,ab,aiweg,aoi,,,,,ia,a,aiwilawf','test.mp3')
	for x in range(0,3):
		finaltext = finaltext = getMashedText(results[0])
		speakSpeechFromText(finaltext,fileName + '.mp3')
		print 'generated ' + fileName + '.mp3'
		fileName += '1'
	fileName = 'tts'
	last_id = results[1]
	time.sleep(30)
