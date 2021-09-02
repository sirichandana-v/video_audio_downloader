from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil


def get_path():
    path=filedialog.askdirectory()
    label_dest.config(text=path)

def download_v():
    video_url=entry_url.get()
    file_path=label_dest.cget("text")
    print("Downloading.......")
    mp4=YouTube(video_url).streams.get_highest_resolution().download()
    video_clip=VideoFileClip(mp4)
    video_clip.close()
    shutil.move(mp4, file_path)
    print("Download completed")

def download_a():
    video_url=entry_url.get()
    file_path=label_dest.cget("text")
    print("Downloading.......")
    mp4=YouTube(video_url).streams.get_highest_resolution().download()
    video_clip=VideoFileClip(mp4)
    audio_file=video_clip.audio
    audio_file.write_audiofile('audio.mp3')
    shutil.move('audio.mp3', file_path)
    audio_file.close()
    video_clip.close()
    
    print("Download completed")

    
    
root=Tk()

root.title('Video and Audio downloader')
canvas=Canvas(root, width=400, height=400)
canvas.pack()

#app label
app_label=Label(root, text="Video and audio downloader", fg='blue')
canvas.create_window(200, 20, window=app_label)

label_url=Label(root, text="Enter the URL")
entry_url=Entry(root)

label_dest=Label(root, text="Select destination path")
button_dest=Button(root, text="select", command=get_path)

button_v=Button(root, text="Download video", command=download_v)
button_a=Button(root, text="Download Audio only", command=download_a)

canvas.create_window(100, 80, window=label_url)
canvas.create_window(250, 80, window=entry_url)
canvas.create_window(100, 120, window=label_dest)
canvas.create_window(250, 120, window=button_dest)
canvas.create_window(100, 160, window=button_v)
canvas.create_window(230, 160, window=button_a)

root.mainloop()
