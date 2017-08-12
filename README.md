# Circle Sound
This repo holds code that has been originally developped for the event ***Les Digitales***, La Chaux-de-Fonds, August 20th 2017.
The idea is to play sounds from a Raspberry Pi based on a distance it measures with an ultrasound distance probe.

All the code is python based, relying on [FluidSynth](www.fluidsynth.org) to generate and play sounds.

More instructions on the assembly to come...

## Dependencies
You need to install FluidSynth on the raspberry, and install the Python wrappers.
```
sudo apt-get install fluidsynth alsa
pip install fluidsynth
```

## Ackowledgment

* The project originated from the ***FabLab in Neuchatel***
* This project was inspired by A.Grove's project [Ultrasonic Pi Piano](http://theotherandygrove.com/projects/ultrasonic-pi-piano/).
* A big shout out to the creators and maintainers of FluidSynth

## License

You are free to use and modify the code here, just know that : 
* It comes as is and there's NO WARRANTY
* FluidSynth is licensed under the LG-license
