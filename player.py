#
# Christian Jaques, august 2017
# This code is based on fluidsynth, www.fluidsynth.org, it is made for the event 
# "Les Digitales" happening at La Tchaux on the 20th of August 2017.
# You may use this code as freely as you wish, as long as you respect fluidsynth's LGL
#
# for help, contact me at :  christian DOT jaques AT gmail DOT com
#
import fluidsynth
import time

# globals
note_max = 127
note_min = 0
dist_max = 120 # 1.2 meters
dist_min = 10 # centimeters

def load_fs():
    ''' starts fluidsynth server and load sound font'''
    fs = fluidsynth.Synth()
    fs.start(driver='alsa')
    sfid= fs.sfload('/usr/share/sounds/sf2/FluidR3_GM.sf2')
    fs.program_select(0,sfid,0,0) # this will also select an instrument!
    
    return fs

def set_sound_settings(fs, channel=0):
    ''' Sets actual sounds settings, such as vibrato, pan, sustain, chorus '''
    fs.cc(channel, 1, 120)
    fs.cc(channel, 93, 120)
    fs.cc(channel, 64, 120)

def convert_dist_to_note(distance):
    ''' Converts the measurement into a note

    It could be useful to calibrate, or set a scale min/max = C to F or so
    '''
    if(distance > dist_min and distance < dist_max):
	# linear interpolation
	note = distance * (note_max-note_min)/(dist_max-dist_min) + note_min
	# set bins ? 
    else:
	note = 0
	print 'Distance is out of bounds'
	print 'distance : ', distance
	print 'min - max distances : ', dist_min, '--', dist_max

    return note
    


# in case module gets launched on its own... sounds like a mechanism I could keep
if __name__ == "__main__":
    note = 0
    fs = load_fs()
    set_sound_settings(fs)

    counter = 0
    d = 23 # first measure 

    # play all notes, to see
    #    for i in range(128):
    #	fs.noteon(0,i,127)
    #	time.sleep(0.1)
    #	fs.noteoff(0,i)
    # IDLE LOOP 
    while(True):
	# measure distance 
	# DEBUG =============== DEBUG
	counter +=1 # just to simulate a measurement
	if(counter % 10 == 0):
		d+= 5
		d %= dist_max
	# DEBUG =============== DEBUG
	n = convert_dist_to_note(d)

	# check it wasn't already playing this note
	if(n != 0): #note):
	    fs.noteoff(0,note)
	    note = n
	    fs.noteon(0,note,127)
        time.sleep(0.5)

