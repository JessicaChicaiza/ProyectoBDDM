
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "DpYQm6f5PImC0e7LZW0CuPFRV"
csecret = "sWTFBzcdWiGsCtjsrQfurWama4qXbFSrRYKM28D7SQKNIVnKQa"
atoken = "4352805022-IHY6aV8a8us864Q8bB6LwD1DhrKnOEn5xaU2ZYy"
asecret = "xWdNWAT5rHZXXS0X0MFxk7zjAP0pPFNjMzSwQC764zlMD"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('guaranda')
except:
    db = server['guaranda']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-79.042023,-1.623015,-78.91391,-1.546136])  #MELBOURNE EAST csv