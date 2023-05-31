'''
Midi Utilities using rtmidi https://www.music.mcgill.ca/~gary/rtmidi/

Tom Zimmerman, IBM Research, CCC
This material is based upon work supported by the NSF under Grant No. DBI-1548297.  
Disclaimer:  Any opinions, findings and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation

# V2 5.31.23 supports channel 
# V1 vel>0 (max 127) to start note at volume=vel
#    set vel=0 to stop note
'''

import rtmidi  # must install this library

# start midi 
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
    print('opened midi port 0')
else:
    midiout.open_virtual_port("My virtual output")
    print('opened midi port virtual')
    
def playChord(ch,key,chord,vel):
    global midiout

    for n in range(len(chord)):
        note=int(chord[n])
        noteOn=[0x90+ch,key+note,vel]
        midiout.send_message(noteOn)
    return

def playNote(ch,note, vel):
    global midiout
    
    noteOn=[0x90+ch,note,vel]
    midiout.send_message(noteOn)
    return    

def changeInstrument(ch,instrumentNumber):
    if instrumentNumber>127:
        print("MIDI ERROR: instrument number",instrumentNumber)
    print('instrument',instrumentNumber)
    cmd=[0xC0+ch,instrumentNumber%127]
    midiout.send_message(cmd)
    return

def quitMidi():
    global midiout
    
    midiout.close_port()    
    del midiout
    print("midi shut down")
    return
