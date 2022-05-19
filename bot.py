import praw
import random
import time


reddit = praw.Reddit(
    client_id='gk6XPeoSoDuLhMa2W3k9cQ',
    client_secret='8JwN1vpUQ-zV_0yyfrN5Nlgzwma99w',
    user_agent='<console: ReadyPost: v1.0.>',
    username='Ready-Post-bot',
    password='Ready123postbot')

subreddit = reddit.subreddit("technology")

startup_quotes = ["We have a “strategic” plan its called doing things. - Steve Jobs",
                "Price is what you pay. Value is what you get. - Elon Musk",
                "Learn early. Learn often. - Drew Houston",
                "You don't need to have a 100-person company to develop that idea. - Larry Page"]

for submission in subreddit.hot(limit=10):
    print("**********")
    print(submission.title)
    
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if "advisory" in comment_lower:
                print("--------")
                print(comment.body)
                random_index = random.randint(0, len(startup_quotes) -1)
                comment.reply(startup_quotes[random_index])
                time.sleep(660)