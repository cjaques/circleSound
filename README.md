# Circle Sound
This repo holds code that has been originally developped for the event ***Les Digitales***, La Chaux-de-Fonds, August 20th 2017.
The idea is to play sounds from a Raspberry Pi based on a distance it measures with an ultrasound distance probe.

All the code is python based, relying on [FluidSynth](http://www.fluidsynth.org) to generate and play sounds.

More instructions on the assembly to come...

### Wire the ultrasound probe
The [ultrasound probe](https://www.sparkfun.com/products/13959) was wired as explained on [this webpage](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi), using two resistors as a dividing bridge to measure the output voltage.

## Dependencies
You need to install FluidSynth on the raspberry, and install the Python wrappers. 
```
sudo apt-get install python-pip fluidsynth alsa
pip install fluidsynth
```

## Usage 
In order to start the project, just run (assuming you have the code in a folder called **circleSound**)
``` 
cd circleSound
./circleSound.py
```

There is a text file called **config.txt** that you may modify, to run different parameters : 
* dist_max : the maximal measured distance
* dist_min : the minimal distance. When something is placed in front of the sensor at a lower distance than dist_min, it will change the played instrument.
* note_min : the lowest played note ***watch out, this HAS to be between [0-127]***
* note_max : the highest played note ***watch out, this HAS to be between [0-127]***
* bins_number : discretization of the measured space. If bins_number = 2, there will be 2 different notes played.
* instrument : the first played instrument. 

## Ackowledgment

* The project originated from the [***FabLab*** in Neuchatel](http://fablab-neuch.ch/)
* This project was inspired by A.Grove's project [Ultrasonic Pi Piano](http://theotherandygrove.com/projects/ultrasonic-pi-piano/).
* A big shout out to the creators and maintainers of FluidSynth

## License

You are free to use and modify the code here, just know that : 
* It comes as is and there's NO WARRANTY
* FluidSynth is licensed under the LGPL
