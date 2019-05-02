from numpy import linspace
class State:
    def __init__(self):
        pass
    
    def getConfigData(self,config):
        resolution=config.resolution

        #state is given access to these 3 so we dont have to pass both state and config to every process in multiprocessing starmap
        self.resolution=resolution
        self.iterations=config.iterations
        self.threshold=config.threshold
        
        xLowerBound,xUpperBound=config.xInitalBounds[0],config.xInitalBounds[1]
        yLowerBound,yUpperBound=config.yInitalBounds[0],config.yInitalBounds[1]

        self.xBounds=(xLowerBound,xUpperBound)
        self.yBounds=(yLowerBound,yUpperBound)

        self.xVals=linspace(xLowerBound,xUpperBound,resolution[0])
        self.yVals=linspace(yLowerBound,yUpperBound,resolution[1])