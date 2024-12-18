from pytube import YouTube

import tkinter as tkinter

from tkinter import filedialog

def download_video(url, save_path):
    try:
       yt = YouTube(url)
       streams = yt.streams.filter(progressive=True, file_extension='mp4')
       highest_res_stream = streams.get_highest_resolution()
       highest_res_stream.download(output_path = save_path)
       print("The video has been downloaded successfully!")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
        return folder
    else:
        print("No folder selected")
        return None
if __name__ == "__main__":
    root = tkinter.Tk()
    root.withdraw()

    url = input("Enter the YouTube video URL: ")
    save_path = open_file_dialog()

    if save_path:
        print("Started Downloading...")
        download_video(url, save_path)
    else:
        print("No folder selected")

