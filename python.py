import praw
import time

r = praw.Reddit(user_agent = "Bot description baba")
r.login("USER","PASSWORD") 

words_to_match = ['hello','i','am','a','list']
cache = []

def run_bot():
    subreddit = r.get_subreddit("subreddit name")
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if isMatch comment.id not in cache and isMatch:
            comment.reply("helllllllo");
            cache.append(comment.id);

while True:
    run_bot()
    time.sleep(10)