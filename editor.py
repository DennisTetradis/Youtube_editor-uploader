from moviepy.editor import *
import os
import random
import time


def edit():
    # load starting clip
    starting_clip = VideoFileClip('videos/100.mp4')

    time = 0
    count = 0
    set_limit = 420 #Time of video!!!
    print("Editing...")
    while time < set_limit:
        count += 1
        clip = VideoFileClip('videos/{}.mp4'.format(count))
        # Add Clip
        if count == 1:
            final = concatenate_videoclips([starting_clip, clip])
        else:
            final = concatenate_videoclips([final, clip])

        time = final.duration



    # write
    clip = VideoFileClip('outro/outro.mp4')
    final = concatenate_videoclips([final, clip])
    final.write_videofile('final/final{}.mp4'.format(len(os.listdir("./final"))+1))

    print('Edit complete!')
    print(time)
    print('Deleting used videos...'+str(count))
    y = 0
    while y < count:
        y += 1
        if os.path.exists('videos/{}.mp4'.format(y)):
            os.remove('videos/{}.mp4'.format(y))
        print("Deleting:"+str(y))

    if os.path.exists('videos/100.mp4'):
        os.remove('videos/100.mp4')
        print("Deleting:100")
