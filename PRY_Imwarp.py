import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import math


###
#PRY_Imwarp class

#Given aircraft and satellite parameters, calculate the x,y offset and rotation

class PRY_Imwarp :
    craft_altitude = 400000 #200KM default
    pixsize_along = 60 #60m alongtrack
    pixsize_across = 60 #60m crosstrack
    framerate = 130


    def __init__(self):
        print ("init function")
        self.test()


    def test (self):
        # given a 1 degree pitch angle
        cpitch = math.radians(.03)
        print ("1 degree is %f radians"%(math.sin(cpitch)))
        yoff = self.craft_altitude * math.tan(cpitch)
        print ("Pitch degree : 1 \t Offset : %f"%(yoff))


    def readAttFile (self, fname) :
        count = 0
        self.pitch=np.zeros(130,dtype=np.float32)
        self.timebig = np.arange(300,300+130, 1./self.framerate)
        self.roll=np.zeros(130, dtype=np.float32)
        self.yaw=np.zeros(130,dtype=np.float32)
        self.time = np.zeros(130, dtype=np.float32)
        fp = open (fname)
        for i in range(300) :
            line = fp.readline()

        for line in fp.readlines():
            sp_line = line.split("\t")
            print ('%s %s %s \r\n'%(sp_line[0], sp_line[1], sp_line[2]))
            self.time[count]=float(sp_line[0])
            self.pitch[count] = float(sp_line[1])
            self.roll[count] = float(sp_line[2])
            self.yaw[count] = float(sp_line[3])
            count = count + 1
            if count >= 130 :
                break
        fp.close()
        #plt.plot (self.time, self.pitch)

        tck = interpolate.splrep (self.time, self.pitch, s=0)
        self.pitchbig = interpolate.splev(self.timebig, tck)
        tck = interpolate.splrep(self.time, self.roll, s=0)
        self.rollbig = interpolate.splev(self.timebig, tck)
        tck = interpolate.splrep(self.time, self.yaw, s=0)
        self.yawbig = interpolate.splev(self.timebig, tck)

        plt.plot(self.timebig, self.pitchbig)
        plt.plot(self.timebig,self.rollbig)
        plt.plot(self.timebig, self.yawbig)
        #plt.xscale((300,800))
        plt.show()
        print (self.ynew.size)
pry = PRY_Imwarp()
pry.readAttFile ('/Users/hg/Desktop/hyti_attfile1.txt')