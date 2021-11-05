import praw
import requests
import requests.auth
from praw.models import MoreComments

from secret_settings import * 

def main():

    reddit = praw.Reddit(
        user_agent = reddit_user_agent,
        client_id = reddit_client_id,
        client_secret = reddit_client_secret,
    )
        
    subreddit = reddit.subreddit("RoastMe")

    with open('corpus.txt', 'w', encoding="utf-8") as f:
        submissions = subreddit.top(limit=10)
        for submission in submissions: 
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                f.write(top_level_comment.body)

            

    

if __name__ == "__main__":
    main()