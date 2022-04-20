# Slicetify

### What is this "Slicetify"

 A tool that fetches song data from any Spotify playlist via the Spotify API and slices the audio file accordingly

![logo](https://raw.githubusercontent.com/innocentDE/Slicetify/main/.github/images/slicetify_logo.png)

## Dependencies

In order to fetch, convert and slice your audio file, you need 

 - [spotify developer account](https://developer.spotify.com/)
 - [pydub](https://pypi.org/project/pydub/)
 ```shell
 pip install pydub
 ```
 - [ffmpeg](https://www.ffmpeg.org/download.html)


## Basic Usage

0) Record your desired playlist (as .mp3) in the correct order in which the songs are sorted by default
1) Create a Spotify application to obtain your Client ID and Client Secret
2) Set your Spotify application credentials as system variables
3) Add ffmpeg to your system Path and edit your path accordingly in the script
4) Copy the playlist ID from your  playlist and edit it in the script
5) Run the script
6) Slices will be put in the output folder