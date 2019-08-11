from ibm_watson import ToneAnalyzerV3
from keys.ibm_keys import *

tone_analyzer = ToneAnalyzerV3(
    version = VERSION,
    iam_apikey = IAM_APIKEY,
    url = URL
)

def containsSad( tweets ):
    for tweet in tweets:
        result = tone_analyzer.tone(tweet)
        
        for tone in result.result['document_tone']['tones']:
            print(str(tone['tone_name']) + ': ' + str(tone['score']))
            if tone['tone_name'] == 'Sadness' and tone['score'] >= 0.7:
                return True
            
        print('\n')

    return False

def find_sad_id( tweets ):
    for tweet in tweets:
        text = tweet.text
        tweet_id = tweet.id

        result = tone_analyzer.tone(text)
        
        for tone in result.result['document_tone']['tones']:
            print(str(tone['tone_name']) + ': ' + str(tone['score']))
            if tone['tone_name'] == 'Sadness' and tone['score'] >= 0.7:
                return tweet_id

    return -1

# ---Test Data---
tweets = []
t1 = 'As long as I can make them laugh, it doesn’t matter how, I’ll be alright. '
t2 = 'I thought, “I want to die. I want to die more than ever before. There’s no chance now of a recovery. No matter what sort of thing I do, no matter what I do, it’s sure to be a failure, just a final coating applied to my shame. That dream of going on bicycles to see a waterfall framed in summer leaves—it was not for the likes of me. All that can happen now is that one foul, humiliating sin will be piled on another, and my sufferings will become only the more acute. I want to die. I must die. Living itself is the source of sin.'

tweets.append(t1)
tweets.append(t2)

#print(containsSad(tweets))