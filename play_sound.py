#Import libraries for opening and playing sounds
from pydub import AudioSegment
from pydub.playback import play


#Open morseshort.mp3 and play it
sound = AudioSegment.from_mp3("morseshort.mp3")
play(sound)
