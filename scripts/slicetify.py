from pydub import AudioSegment

# lol, i dont know how I keep track of this fucking mess

# Edit to your song path
song = AudioSegment.from_file("C:\\Users\\vince\\Desktop\\pydub\\song.wav")
# Edit to your ffmpeg path
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"

half_song = len(song) // 2
output = song[:half_song]

output.export("C:/Users/vince/Desktop/pydub/output.mp3", format="mp3")