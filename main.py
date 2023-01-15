from datetime import date
import time
from upload_video import upload_video
from rename import rename_clips
from editor import edit


video_count = 0
def get_video_data():
    video_count += 1
    
    video_data = {
        "file": "./final/final{}.mp4".format(video_count),
        "title": "Bullticks {}".format(video_count),
        "description": "#shorts\nGiving you the hottest memes of the day with funny comments!",
        "keywords":"meme,reddit,Dankestmemes",
        "privacyStatus":"public"
    }


print(video_data["title"])
print("Posting Video...")
upload_video(video_data)
time.sleep(2)

rename_clips()
edit()
