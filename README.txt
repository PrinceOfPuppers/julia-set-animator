#julia-set-animator

dependencies:
    -matplotlib
    -numpy

description:
    generates an animation of julia sets according to a path of seedpoints defined parametrically
    set in config.py

    multiprocessing is used to decrease the image rendering time, this is incredibly helpful due to 
    the large number of iterations needed to obtain a good resolution with certain julia sets

    the process uses alot of memory, as such it will reach the 32 bit python memory limit if a resolution
    of 2000 by 2000 with 160 frames is used

    the decision to save animations must be done BEFORE rendering, by changing a setting in config.py
    however to do this you must have imageMagick installed on your computer
