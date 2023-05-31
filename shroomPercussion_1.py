# -*- coding: utf-8 -*-
"""
Tom Zimmerman, IBM Research, CCC

Dataset: Split gill fungi Schizophyllum commune
https://royalsocietypublishing.org/doi/10.1098/rsos.211926
https://zenodo.org/record/5790768

This material is based upon work supported by the NSF under Grant No. DBI-1548297.  
Disclaimer:  Any opinions, findings and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation
"""
import numpy as np
import playNoteChord_2 as M
import time 

duration=.16 # how long note plays

fileName=r'C:/Users/820763897/Documents/Docs/PROJECTS/CCC/Exploratorium/Mushrooms/Schizophyllum 5-6 offset.csv'
    
shrume=np.loadtxt(fileName,delimiter=',')
maxSignal=shrume.max()
notesInSignal=24
step=maxSignal/notesInSignal

key=60
lastNote=-1
ch=9 # 1=kbd, 9= drums
for i in range(len(shrume)):
    v=shrume[i]
    s=int(v/step)
    note=key+s
    if note!=lastNote:
        M.changeInstrument(ch,note%127)
        M.playNote(ch,note,127)
        time.sleep(duration)
        M.playNote(ch,note,0)   
    lastNote=note
    
M.quitMidi()    
print('Midi port closed')