#the set of all points of convergence for the
#function f_c (z)=z^2 +c, which is composed with
#itself n times (n approches inf)

def iterate(z,c):
    nextZ=z**2+c
    return(nextZ)

def didConvergeAtZWithRate(z,c,iterations,threshold):
    #iterates a until modulus a is greather than the
    #threshold, or until it reaches the max number of iterations
    for i in range(1,iterations+1):
        z=iterate(z,c)
        magA=(z.real)**2+(z.imag)**2
        if magA>threshold:
            return(i)
    return(0)


#used by pool.starmap() for multiprocessing
def calculateImageArrayRow(yIndex,imageRow,state):
    c=state.currentSeedPoint
    iterations=state.iterations
    threshold=state.threshold

    for xIndex in range(0,state.resolution[1]):
        z=state.xVals[xIndex]+state.yVals[yIndex]*1j
        iterationsTillDivergence=didConvergeAtZWithRate(z,c,iterations,threshold)

        #the square root gives better dynamic range in the color map
        #it is needed here due to the high number of iterations
        #required by the julia sets
        imageRow[xIndex]=(iterationsTillDivergence/iterations)**(1/2)
    return(imageRow)

def populateImageArray(imageArray,config,state):
    resolution=config.resolution
    iterations=config.iterations
    threshold=config.threshold
    c=state.currentSeedPoint

    if config.enableMultiProcessing:

        p=Pool(config.processesUsed)
        rowsPerChunk=int(ceil(resolution[0]/(8*config.processesUsed)))
        iterable=[]
        for yIndex,row in enumerate(imageArray):
            iterable.append((yIndex,row,state))
        imageArray=p.starmap(calculateImageArrayRow,iterable,chunksize = rowsPerChunk)

        p.close()
        p.join()
    
    else:
        for xIndex in range(0,resolution[0]):
            print(xIndex)
            for yIndex in range(0,resolution[1]):
                z=state.xVals[xIndex]+(state.yVals[yIndex])*1j
                
                #the square root gives better dynamic range in the color map
                #it is needed here due to the high number of iterations
                #required by the julia sets
                imageRow[xIndex]=(iterationsTillDivergence/iterations)**(1/2)
    return(imageArray)

def createColorJulia(config,state):
    resolution=config.resolution
    imageArray=zeros((resolution[0], resolution[1]), dtype=float)
    imageArray=populateImageArray(imageArray,config,state)
    return(imageArray)

def animateColorJulia(config,state):
    frameList=[]
    fig=plt.figure()
    for frameNumber,t in enumerate(config.tVals):
        print("rendering frame",frameNumber+1)
        config.parametricSeedPoint(t,state)

        x1,x2=state.xBounds[0],state.xBounds[1]
        y1,y2=state.yBounds[0],state.yBounds[1]
        imageArray=createColorJulia(config,state)
        norm=mpl.colors.Normalize(vmin=0,vmax=1)
        frame=plt.imshow(imageArray,origin='lower',cmap='hot', aspect='equal', interpolation='nearest',extent=[x1,x2,y1,y2], animated=True,norm=norm)

        frameList.append([frame])
    animation=ani.ArtistAnimation(fig,frameList,interval=(1000/config.framerate))
    if config.saveAnimaiton:
        animation.save('./saved animations/julia.gif',writer='imagemagick')
    plt.show()

def main(config,state):
    animateColorJulia(config,state)

if __name__ == "__main__":
    from numpy import linspace,zeros,array
    from math import ceil
    from multiprocessing import Pool
    import matplotlib.pyplot as plt
    import matplotlib.animation as ani
    import matplotlib as mpl
    from config import Config
    from state import State

    config=Config()
    state=State()
    state.getConfigData(config)

    main(config,state)