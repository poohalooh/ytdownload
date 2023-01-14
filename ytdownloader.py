from pytube import YouTube
import sys
from tkinter import filedialog
from tkinter import *

link = input('Enter the link of a video to download: ')

def show_progress_bar(stream, chunk, bytes_remaining):
  current = ((stream.filesize - bytes_remaining)/stream.filesize)
  percent = ('{0:.1f}').format(current*100)
  progress = int(50*current)
  status = '█' * progress + '-' * (50 - progress)
  sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
  sys.stdout.flush()

file_name = input('Enter desired filename: ')

yt = YouTube(link)

def folder_select():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

folder_select()

yt.register_on_progress_callback(show_progress_bar)
yt.streams.get_audio_only().download(folder_selected, file_name + '.mp4')

print('Audio was successfully downloaded.')