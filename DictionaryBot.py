import praw
import time

r = praw.Reddit(user_agent =
	"Dictionary Bot defines words for you! /u/The_Dictionary_Bot")

#retrieve login information from login.txt
try:
	#open filestream
	login = open("login.txt","r")
	cache = open("cache.txt","w")
except IOError:
	print("There was an error getting read/write files")
	sys.exit()

print("Logging in...")
username = login.readline()
password = login.readline()
login.close()

r.login(username,password)
print("Logged in!")

match=["define:"]

def bot_run():
	print("Searching comments...")
	subreddit = r.get_subreddit("test")
	comments = subreddit.get_comments(limit = 50)
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in match)
		if isMatch:
			print("Comment found! Replying...")
			comment.reply("The definition of 'cat ' is a small domesticated "+
				"carnivorous mammal with soft fur, a short snout, and retrac"+
				"tile claws. It is widely kept as a pet or for catching mice,"+
				" and many breeds have been developed.")
			cache.write(comment.id)
			cache.write("\n")

while True:
	bot_run()
	time.sleep(5)

	

