import praw
import SSSSH
import matplotlib.pyplot as plt
reddit = praw.Reddit(
    client_id=SSSSH.client_id,
    client_secret=SSSSH.client_secret,
    user_agent="boobs_lover69 (By /u/jurgen112)",
)
wordCount = {}

sub = "anime"
subreddit = reddit.subreddit(sub)
commonWords = {'that','this','and','of','the','for','I','it','has','in',
'you','to','was','but','have','they','a','is','','be','on','are','an','or',
'at','as','do','if','your','not','can','my','their','them','they','with',
'at','about','would','like','there','You','from','get','just','more','so',
'me','more','out','up','some','will','how','one','what',"don't",'should',
'could','did','no','know','were','did',"it's",'This','he','The','we',
'all','when','had','see','his','him','who','by','her','she','our','thing','-',
'now','what','going','been','we',"I'm",'than','any','because','We','even',
'said','only','want','other','into','He','what','i','That','thought',
'think',"that's",'Is','much',"1","2","3","4","5"}

for submission in subreddit.top(limit=1):
    submission.comments.replace_more(limit=0) 
    for comment in submission.comments:
        split = comment.body.strip().lower().split(" ")
        for word in split:
            if word in commonWords: continue

            if word not in wordCount: wordCount[word] = 0
            wordCount[word] += 1

bruh = sorted(wordCount.items(), key=lambda x:x[1], reverse=True)

labels = []
data = []

for i in range(10):
    labels.append(bruh[i][0])
    data.append(bruh[i][1])

print(labels)
print(data)

plt.title('Top comments for: r/' + sub)
plt.pie(data, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("POG.png")