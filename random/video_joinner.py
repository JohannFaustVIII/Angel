from moviepy.editor import *

video = ""

files = []

while True:
    video = input("Video to add: ")
    if video == 'q':
        break
    files.append(VideoFileClip(video))

output_file = input("Output file: ")

final_clip = concatenate_videoclips(files)
final_clip.to_videofile(output_file, fps=60, remove_temp=True)