#!/usr/bin/python

def next_note(note):
# note can be A,B,C,D,E,F,G
	if note == 'G':
		return 'A'
	else:
		return chr(ord(note)+1)

def next_semitone(semitone):
# semitone can be A,A#,B,C,C# etc.
	if len(semitone)>1 :
		if semitone[1] == '#':
			return next_note(semitone[0])
	if semitone[0] == 'B':
		return 'C'
	if semitone[0] == 'E':
		return 'F'
	return semitone[0] + '#'

def next_nth_semitone(semitone, n):
	for i in range(n):
		semitone = next_semitone(semitone)
	return semitone

def next_pitch(pitch):
# pitch can be A0,A#0,C4 etc.
	if pitch[1] == '#':
		semitone = pitch[:2]
		octave = int(pitch[2:])
	else:
		semitone = pitch[0]
		octave = int(pitch[1:])
	semitone = next_semitone(semitone)
	if semitone == "C":
		octave = octave+1
	return semitone + str(octave)

def next_stream(init, function, size):
	stream = []
	for i in range(size):
		stream.append(init)
		init=function(init)
	return stream

def major_chord(note):
	print note+" chord:"
	print note,next_nth_semitone(note, 4),next_nth_semitone(note, 7)

def minor_chord(note):
	print note+"m chord:"
	print note,next_nth_semitone(note, 3),next_nth_semitone(note, 7)

# Samples

# Guitar with standard tuning (fret 0 is open fret)
print next_stream("E4", next_pitch, 13)
print next_stream("B3", next_pitch, 13)
print next_stream("G3", next_pitch, 13)
print next_stream("D3", next_pitch, 13)
print next_stream("A2", next_pitch, 13)
print next_stream("E2", next_pitch, 13)

major_chord("A")
minor_chord("B")
