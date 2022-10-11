from pytube import YouTube
import os
import sys

def download(link : str, output_directory : str, file_name : str, music_only : bool):
    yt = YouTube(url=link)
    if music_only:
        yt = yt.streams.filter(only_audio=True).first()
    else:
        yt = yt.streams.get_highest_resolution()

    try:
        out_file = yt.download(output_path=output_directory)
    except Exception as e:
        print("Download failed!")
        print(e)
        return

    new_file = output_directory + os.sep + file_name + ".mp4"
    os.rename(out_file, new_file)
    
    print("Download finished.")

if __name__ == "__main__":
    music_options = ["m", "music"]
    video_options = ["v", "video"]

    link = input("Download URL: ")
    extension = input("As video or music [m/v]:").lower()

    if extension not in music_options and extension not in video_options:
        print("Wrong extension")
        sys.exit(0)

    output_dir = input("Output directory: ")
    output_file = input("File name: ")
    download(link, output_dir, output_file, extension in music_options)

    