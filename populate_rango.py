import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YouPy.settings')

import django
django.setup()

from rango.models import Video

def populate():
    
    add_video(videoid="s6HB5nMtqT4",
        url="https://www.youtube.com/watch?v=s6HB5nMtqT4")
    
    add_video(videoid="0STb5f-QkCU",
        url="https://www.youtube.com/watch?v=0STb5f-QkCU")
    
    add_video(videoid="MwYYBd8RUl0",
        url="https://www.youtube.com/watch?v=MwYYBd8RUl0")
    
    add_video(videoid="D9xuwqTwx3E",
        url="https://www.youtube.com/watch?v=D9xuwqTwx3E")

    # Print out what we have added to the user.
    for v in Video.objects.all():
        print "- {0}".format(str(v))

def add_video(videoid, url):
    v = Video.objects.get_or_create(videoid=videoid, url=url)[0]
    return v


# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
    