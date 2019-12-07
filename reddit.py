import time
import praw
import json

from praw.models import MoreComments


reddit = praw.Reddit(client_id='k3RhtziKnOwLEA',
                     client_secret='Wu3jO-k9leAmqm0w28isM9i_mmI',
                     password='Qwertyui9',
                     user_agent='testscript by',
                     username='digitalfootprintINF')

#submission = reddit.submission(url='https://www.reddit.com/r/GreenBayPackers/comments/do1a50/week_8_game_thread_green_bay_packers_kansas_city/')
submission = reddit.submission(id='drb0c1')
submission.comments.replace_more(limit=0)
allCommentsList = []
#type = "game"
type = "post-game"

for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    comment = {}
    comment["author"] = str(top_level_comment.author)
    comment["comment"] = str(top_level_comment.body)
    comment["likes"] = str(top_level_comment.score)
    comment["created_time"] = str(top_level_comment.created)
    comment["thread-type"] = type 
    allCommentsList.append(comment)

jsonText = json.dumps(allCommentsList)
print(jsonText)

