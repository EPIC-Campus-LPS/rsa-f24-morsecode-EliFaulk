#Import libraries for opening and playing sound
from pydub import AudioSegment
from pydub.playback import play


#Open morseshort.mp3 and morselong.mp3
short = AudioSegment.from_mp3("morseshort.mp3")
long = AudioSegment.from_mp3("morselong.mp3")


#Play loops for each letter in morse
#H
for i in range(4):
	play(short)
#E
play(short)
#LL
for i in range(2):
	play(short)
	play(long)
	play(short)
	play(short)
#O
for i in range(3):
	play(long)


