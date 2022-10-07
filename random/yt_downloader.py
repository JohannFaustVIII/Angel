from pytube import YouTube
import os

def download(link : str, output_directory : str, file_name : str, extension : str):
    yt = YouTube(url=link)
    if extension == "mp3":
        yt = yt.streams.filter(only_audio=True).first()
    elif extension == "mp4":
        yt = yt.streams.get_highest_resolution()
    else:
        print("Wrong extension passed")
        return

    try:
        out_file = yt.download(output_path=output_directory)
    except Exception as e:
        print("Download failed!")
        print(e)
        return

    new_file = output_directory + os.sep + file_name + "." + extension
    os.rename(out_file, new_file)
    
    print("Download finished.")

link = input("Download URL: ")
extension = input("As mp3 or mp4? ") # this mp3 is redundant as music can be in mp4 too? should be slightly different
if extension in ["mp3", "mp4"]:
    output_dir = input("Output directory: ")
    output_file = input("File name: ")
    download(link, output_dir, output_file, extension)
else:
    print("Wrong extension")