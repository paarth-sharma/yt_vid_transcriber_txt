### Setup for windows
```
#setup a virtual env and install stuff in it locally
python -m venv venv
.\venv\Scripts\activate

pip install requests yt_dlp
```

Downloading and converting YouTube videos to audio formats without ffmpeg can be challenging, as yt-dlp relies on ffmpeg for tasks like format conversion and merging audio and video streams. 

install Scoop it has a wide range of windows builds and toolkits that you might have to build from scratch which can be challenging. 
Scoop automatically creates path variables and symlinks for executables.
Instead run in your powershell (you make have to adjust permissions):
```
#install scoop for windows
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression 

#then just install ffmpeg with scoop
scoop install ffmpeg
```

now run the file and you'll get the txt file.
```
python yt_to_txt.py
```