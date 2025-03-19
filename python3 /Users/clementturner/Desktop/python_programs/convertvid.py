import yt_dlp
from moviepy.editor import *
import os
from pathlib import Path
import time
import sys

def download_and_convert_to_wav(youtube_url, output_path=None, custom_title=None):
    try:
        # Create filename using custom title or timestamp
        video_title = custom_title if custom_title else f"ytvideo_{int(time.time())}"
        
        # Set default output path to Music folder
        if output_path is None:
            output_path = str(Path.home() / "Music")
        
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, f"{video_title}.%(ext)s"),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
            'quiet': True,
            'no_warnings': True
        }
        
        # Download and convert to WAV
        print(f"Downloading and converting: {video_title}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        
        print(f"Conversion complete! File saved as: {os.path.join(output_path, f'{video_title}.wav')}")
        return os.path.join(output_path, f"{video_title}.wav")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 convertvid.py <YouTube URL> [custom_title]")
        sys.exit(1)
    
    # Get URL from command line argument
    url = sys.argv[1]
    
    # Get custom title if provided
    custom_title = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Download and convert
    download_and_convert_to_wav(url, custom_title=custom_title)
