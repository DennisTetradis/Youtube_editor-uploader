from moviepy.editor import *
import os
import random
import time

# Directory where the files are located
directory = './Exports'

# Get a list of all the files in the directory
files = os.listdir(directory)

# Shuffle the list of files
random.shuffle(files)

# Loop through the files
for i, file in enumerate(files):
    # Construct the new file name
    new_name = 'files{}.mp4'.format(i + 1)

    # Get the full path of the file
    old_path = os.path.join(directory, file)

    # Construct the full path of the new file name
    new_path = os.path.join(directory, new_name)

    # Rename the file
    os.rename(old_path, new_path)

time.sleep(1)

# Directory where the files are located
directory = './Exports'

# Get a list of all the files in the directory
files = os.listdir(directory)

# Shuffle the list of files
random.shuffle(files)

# Loop through the files
for i, file in enumerate(files):
    # Construct the new file name
    new_name = '{}.mp4'.format(i + 1)

    # Get the full path of the file
    old_path = os.path.join(directory, file)

    # Construct the full path of the new file name
    new_path = os.path.join(directory, new_name)

    # Rename the file
    os.rename(old_path, new_path)

# load starting clip
starting_clip = VideoFileClip('Exports/60.mp4')

time = 0
count = 0
set_limit = 420 #Time of video

while time < set_limit:
    count += 1
    clip = VideoFileClip('Exports/{}.mp4'.format(count))
    # Add Clip
    if count == 1:
        final = concatenate_videoclips([starting_clip, clip])
    else:
        final = concatenate_videoclips([final, clip])

    time = final.duration
    print(time)


# write
final.write_videofile('combined.mp4')

print('Edit complete!'+str(count))

y = 0
while y < count:
    y += 1
    if os.path.exists('Exports/{}.mp4'.format(y)):
        os.remove('Exports/{}.mp4'.format(y))
    print("Deleting:"+str(y))

if os.path.exists('Exports/60.mp4'):
    os.remove('Exports/60.mp4')
    print("Deleting:60")
