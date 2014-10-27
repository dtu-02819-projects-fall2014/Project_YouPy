from config import USERNAME,PASSWORD,COMMENTS_PATH, WORDS_PATH
from gdata.youtube import service
from os import remove
#from models import Video

#VIDEO_ID    =  Video.objects.get(pk=1)
#URL_PATTERN = "https://gdata.youtube.com/feeds/api/videos/D9xuwqTwx3E/comments?orderby=published&start-index=1&max-results=25"
VIDEO_ID    =  '9bZkp7q19f0'

remove(COMMENTS_PATH)
remove(WORDS_PATH)

def comments_generator(client, video_id):
    #comment_feed = client.GetYouTubeVideoCommentFeed(uri=URL_PATTERN,video_id=video_id)
    comment_feed = client.GetYouTubeVideoCommentFeed(video_id=video_id)
    count_comments = 0
    while comment_feed is not None:
        for comment in comment_feed.entry:
            count_comments = count_comments+1 
            print 'Writing comment number '+str(count_comments)+'...'
            yield comment
        next_link = comment_feed.GetNextLink()
        
        if next_link is None:
            print '\nMining comments done...\nTotal number of comments: '+str(count_comments)+'\n'
            comment_feed = None
        else:
            comment_feed = client.GetYouTubeVideoCommentFeed(next_link.href)

client = service.YouTubeService()
client.ClientLogin(USERNAME, PASSWORD)

for comment in comments_generator(client, VIDEO_ID):
    author_name = comment.author[0].name.text
    text = comment.content.text
    
    with open(COMMENTS_PATH, 'a+') as c:
        #Convert text to str and remove newlines        
        single_comment = str(text).replace("\n", " ")
        single_comment+='\n'
        c.write(single_comment)
        with open(WORDS_PATH,'a+') as w:
            words=[]
            words = single_comment.split()
            for word in words:
                single_word = str(word)
                single_word+='\n'
                w.write(single_word)            
w.close()
c.close()    
