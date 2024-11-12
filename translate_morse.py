#Import libraries for opening and playing sound
from pydub import AudioSegment
from pydub.playback import play


#Dictionary of each letter and number in morse code
alphabet = {
    'A': ['short', 'long'],
    'B': ['long', 'short', 'short', 'short'],
    'C': ['long', 'short', 'long', 'short'],
    'D': ['long', 'short', 'short'],
    'E': ['short'],
    'F': ['short', 'short', 'long', 'short'],
    'G': ['long', 'long', 'short'],
    'H': ['short', 'short', 'short', 'short'],
    'I': ['short', 'short'],
    'J': ['short', 'long', 'long', 'long'],
    'K': ['long', 'short', 'long'],
    'L': ['short', 'long', 'short', 'short'],
    'M': ['long', 'long'],
    'N': ['long', 'short'],
    'O': ['long', 'long', 'long'],
    'P': ['short', 'long', 'long', 'short'],
    'Q': ['long', 'long', 'short', 'long'],
    'R': ['short', 'long', 'short'],
    'S': ['short', 'short', 'short'],
    'T': ['long'],
    'U': ['short', 'short', 'long'],
    'V': ['short', 'short', 'short', 'long'],
    'W': ['short', 'long', 'long'],
    'X': ['long', 'short', 'short', 'long'],
    'Y': ['long', 'short', 'long', 'long'],
    'Z': ['long', 'long', 'short', 'short'],
    '0': ['long', 'long', 'long', 'long', 'long'],
    '1': ['short', 'long', 'long', 'long', 'long'],
    '2': ['short', 'short', 'long', 'long', 'long'],
    '3': ['short', 'short', 'short', 'long', 'long'],
    '4': ['short', 'short', 'short', 'short', 'long'],
    '5': ['short', 'short', 'short', 'short', 'short'],
    '6': ['long', 'short', 'short', 'short', 'short'],
    '7': ['long', 'long', 'short', 'short', 'short'],
    '8': ['long', 'long', 'long', 'short', 'short'],
    '9': ['long', 'long', 'long', 'long', 'short']
}


#Open morseshort.mp3 and morselong.mp3
short = AudioSegment.from_mp3("morseshort.mp3")
lng = AudioSegment.from_mp3("morselong.mp3")


#Take input and play corresponding morse code for each letter
message = input("Input: ").upper()

for i in message: 
	print(i)
	for x in alphabet[i]:
		if x == "short":
			play(short)
		elif x == "long":
			play(lng)



