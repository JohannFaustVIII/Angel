from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def timestamp_to_seconds(timestamp: str) -> int:
    time = 0
    for t in timestamp.split(":"):
        time = time * 60 + int(t)
    return time

input_video = input("Input: ")
start = input("Start timestamp: ")
end = input("End timestamp: ")
output_video = input("Output: ")

start_second = timestamp_to_seconds(start)
end_second = timestamp_to_seconds(end)

ffmpeg_extract_subclip(input_video, start_second, end_second, targetname=output_video)