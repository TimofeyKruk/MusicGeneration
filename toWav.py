import os
import pydub

#pydub.AudioSegment.converter = r"C:\\path\\to\\ffmpeg.exe"
# Converting mp3 to WAV format
path="F:\BSU_FAMCS\Learning_Courses\musicGenerator\dataset"
savepath="F:\\BSU_FAMCS\\Learning_Courses\\musicGenerator\\dataset\\WAV\\"

for song in [element for element in os.listdir(path) if "mp3" in element]:
    print(path+song)
    file=open(path+'\\'+song)
    sound=pydub.AudioSegment.from_mp3(path+'\\'+song)
    sound.export(savepath+'\\'+song.replace(".mp3",".wav"),format="wav")

