# YouTube to WAV Converter

A Python script that downloads YouTube videos and converts them to WAV audio files.

## Requirements
- Python 3.x
- FFmpeg
- Required Python packages:

yt-dlp moviepy

## Installation
1. Clone this repository or download the script
2. Install FFmpeg (on MacOS):
 ```bash
 brew install ffmpeg
```

To install the required Python packages:
```bash
pip install -r requirements.txt
```
## Usage

-To run the program from Terminal:
```bash
python3 convertvid.py <YouTube URL> [custom_title]
```
Here is an example:
```bash
python3 convertvid.py "https://www.youtube.com/watch?v=example" "my_song"
```
The converted WAV file will be saved in ~/Music

