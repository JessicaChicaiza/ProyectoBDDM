
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "YVkYByHezfSGGY8Ti2KAEOJxL"
csecret = "JxhODU70W39fbxpoKHSLrAKEvL241Hq4DRYbswbbMXsrnSrPUb"
atoken = "735576340510965761-elbrewFhsme3ozu75xXK0Vl1okfwRfU"
asecret = "iNQlEZEiQYXqStLMPo8mGwZLh7DOXlqK4uA9RnQVOXU3p"
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
    db = server.create('galapagos')
except:
    db = server['galapagos']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-92.0085,-1.4114,-89.2409,1.6816])  #MELBOURNE EAST csv