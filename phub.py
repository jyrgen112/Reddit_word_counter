import praw
import SSSSH
reddit = praw.Reddit(
    client_id=SSSSH.client_id,
    client_secret=SSSSH.client_secret,
    user_agent="boobs_lover69 (By /u/jurgen112)",
)

for i in reddit.subreddit("Anime").new(limit=10):
    print(i.title)