import argparse
from pytube import YouTube
import sys

parser = argparse.ArgumentParser(prog="ytdownload", description = 'Download audio stream from a YouTube video.')

parser.add_argument('-u', '--url', required=True, help='Link for a video to download audio from. Must be in doublequotes')
parser.add_argument('-d', '--dir', required=True, help='Saves the directory of the final file')
parser.add_argument('-f', '--file', required=True, help='Name of the final file')

args = parser.parse_args()

yt = YouTube(args.url)

def show_progress_bar(stream, chunk, bytes_remaining):
  current = ((stream.filesize - bytes_remaining)/stream.filesize)
  percent = ('{0:.1f}').format(current*100)
  progress = int(50*current)
  status = '█' * progress + '-' * (50 - progress)
  sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
  sys.stdout.flush()

yt.register_on_progress_callback(show_progress_bar)
yt.streams.get_audio_only().download(args.dir, args.file + '.mp4')
