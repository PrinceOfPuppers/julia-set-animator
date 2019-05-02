from numpy import linspace,pi,sin,cos
from multiprocessing import cpu_count
class Config:
    def __init__(self):
        self.resolution=(1000,1000)

        #only enable if you have imageMagick installed
        self.saveAnimaiton=True

        tRange=(0,2*pi)
        totalFrames=160
        self.framerate=30

        #julia sets typically need a high number of iterations to look proper, this number also depends on what resolution is set
        self.iterations=1000
        self.threshold=4

        self.enableFullScreen=True

        #mutiProcessing only supported for color mandelbrot
        self.enableMultiProcessing=True

        #the number of processes spawned is determined by cpu count, change if you wish
        self.processesUsed=cpu_count()

        #starting screen (yUpperBound is calculated to keep it square)
        xLowerBound=-2
        xUpperBound=2

        yLowerBound=-2

        #after each click zoom, how big is the screen compared to last time
        self.newWindowSize=1/2

        #non adjustable
        yUpperBound=yLowerBound+(xUpperBound-xLowerBound)
        self.xInitalBounds=(xLowerBound,xUpperBound)
        self.yInitalBounds=(yLowerBound,yUpperBound)

        self.tVals=linspace(tRange[0],tRange[1],totalFrames)

    def parametricSeedPoint(self,t,state):
        #nice path i found on wikipedia, change to whatever path you like to
        #explore more of the julia set
        c=0.7885*(cos(t)+1j*sin(t))
        state.currentSeedPoint=c
    