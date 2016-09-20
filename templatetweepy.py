#Template that execute tweppy module, authenticate with twitter and gets ready to execute the api.
#Begin Import of Libraries and Variables Definition.
import tweepy
cKey = "x"
cSec = "y"
cWeb = "z"
cCod = "p"
cAut = "s"
#Begins with human interfacing
cKey = input("Write the Consumer Key ")
cSec = input("Write the Consumer Secret ")
auth = tweepy.OAuthHandler(cKey, cSec)
cWeb = auth.get_authorization_url()
print("In your browser go and check for your code at:",cWeb)
print("then copy paste the number next")
cCod = input("what was that number?")
auth.get_access_token(cCod)
api = tweepy.API(auth)

for friend in tweepy.Cursor(api.friends).items():
    process_friend(friend)
