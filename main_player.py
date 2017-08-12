# 
# This code plays music based on a measured distance. 
# The sound is generated using FluidSynth, www.fluidsynth.org
# Originally made for "Les Digitales" at la Chaux-De-Fond, August 20th 2017.
#
# christian DOT jaques AT gmail DOT com
#
# feel free to do whatever with this code, as long as your respect fluidsynth's LG-license.
# 
import RPi.GPIO as GPIO
import fluidsynth
import time

# globals
note_max = 117
note_min = 0
dist_max = 140 # cm
dist_min =  10 # cm

# GPIOs
TRIG = 24
ECHO = 23


def init_GPIO():
    ''' Sets measure GPIOS and others if needed'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def cleanup():
    GPIO.cleanup()

def setup_probe():
    ''' Setup ultrasound probe'''
    GPIO.output(TRIG,False)
    time.sleep(2)

def measure_distance():
    ''' Returns measured distance in cm '''
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) ==0:
        pulse_start = time.time()

    while GPIO.input(ECHO) ==1:
        pulse_end = time.time()

    try:
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance,2)
    except Exception as e :
	print 'Caught stuff, exception : ', e
	# re-measure distance
	measure_distance()


    return distance

def load_fs(instrument):
    ''' starts fluidsynth server and load sound font'''
    fs = fluidsynth.Synth()
    fs.start(driver='alsa')
    sfid= fs.sfload('/usr/share/sounds/sf2/FluidR3_GM.sf2')
    fs.program_select(0,sfid,0,instrument) # this will also select an instrument!

    return fs, sfid

def change_instrument(sfid, instrument):
    ''' Sets another instrument '''
    fs.program_select(0,sfid,0,instrument)
    print 'Instrument is number : ', instrument

def set_sound_settings(fs, channel=0):
    ''' Sets actual sounds settings, such as vibrato, pan, sustain, chorus '''
    fs.cc(channel, 1, 1)
    fs.cc(channel, 93, 1)
    fs.cc(channel, 64, 1)

def convert_dist_to_note(distance):
    ''' Converts the measurement into a note

    It could be useful to calibrate, or set a scale min/max = C to F or so
    '''
    if(distance > dist_min and distance < dist_max):
	# linear interpolation
	note = distance * (note_max-note_min)/(dist_max-dist_min) + note_min
	# set bins ? 
    elif(distance < dist_min):
	note = 0
    else :
	note = note_max


    return note


# in case module gets launched on its own... sounds like a mechanism I could keep
if __name__ == "__main__":
    note = 0
    instrument = 0
    # init FluidSynth and sound font library
    fs, sfid = load_fs(instrument)
    set_sound_settings(fs)
    # init GPIO and ultraprobe
    init_GPIO()
    setup_probe()

    counter = 0
    d = 23 # first measure 

    # IDLE LOOP 
    while(True):
	# measure distance 
	d = measure_distance()
	print 'Distance is : ', d, 'cm'
	n = int(convert_dist_to_note(d))
	if (n==0):
	    instrument +=1
	    instrument %= 42
	    change_instrument(sfid, instrument)
	print 'Play note : ', n

	# check it wasn't already playing this note
	if(n != 0): #note):
	    fs.noteoff(0,note)
	    note = n
	    fs.noteon(0,note,127)
        time.sleep(0.5)

