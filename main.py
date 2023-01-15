from datetime import date
import time
from upload_video import upload_video
from rename import rename_clips
from editor import edit


def get_video_data(count):
    count += 1
    
    video_data = {
        "file": "./final/final{}.mp4".format(count),
        "title": "Bulltiks {}".format(count),
        "description": "Best of Memes\nI am just trying to make you laugh!\nI hope you like😜",
        "keywords":"meme,reddit,Dankestmemes",
        "privacyStatus":"public"
    }
    return (count, video_data)


while True:
    video_count = 0
    video_count, video_data = get_video_data(video_count)
    print(video_data)
    print("Posting Video...")
    rename_clips()
    edit()
    time.sleep(60)
    upload_video(video_data)
    time.sleep(302400)

