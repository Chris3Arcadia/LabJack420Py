# # Python Class for reading 4-20mA transmitted signals using a LabJack T7
#
# By Chris Arcadia (2021/05/30)
#
# Intended for use with the LabJack T7
#
# Inspired by the following Repositories: 
#   * "simple_log.py" (from "supplementary-ljm-examples" by LabJack: https://github.com/labjack/supplementary-ljm-examples/tree/master/python/simple_log.py)

from labjack import ljm
import os
import sys
import time
import datetime
import numpy
from matplotlib import pyplot

class LabJack420Py():

    def __init__(self):
        self.load_options()
        self.load_constants()
        self.set_path()    
        self.initialize_system()
        self.initialize_channel()

    def load_options(self):
        self.verbose = True # enable detailed command line messages
        self.model = "T7" # device model 
        self.connection = "ANY" # connection type
        self.identifier = "ANY" # device identifier
        self.channel = "AIN0" # analog input channel       
        self.resolution = 8 # resolution setting for the analog channel: 0-8 for T7, 0-12 for T7-Pro. Default value of 0 corresponds to an index of 8 (T7) or 9 (T7-Pro).
        self.range = 10 # measure range setting for the analog channel: 0.0=Default => +/-10V, 10.0 => +/-10V, 1.0 => +/-1V, 0.1 => +/-0.1V, or 0.01 => +/-0.01V.
        self.rate = 100*1e3 # acquisition rate for the analog channel in microseconds 
        self.resistance = 250 # resistance of shunt used to measure the 4-20mA signal in ohms

    def load_constants(self):
        # load constants specific to Blackfly

        self.hardware = {
            'interface':'USB 3', 
            'manufacturer': 'LabJack', 
            'device': self.model,
        } # known hardware details

        self.units = {
            'time': 's',
            'voltage': 'V',
            'current': 'A',            
        }           

    def set_path(self,pathOut=None):
        self.path = dict();        
        self.path['root'] = os.path.dirname(__file__)
        if not pathOut:
            # provide default output path
            pathOut = os.path.join(self.path['root'],'__temporary__')      
            self.ensure_path(pathOut)                
        self.path['output'] = pathOut                            

    def ensure_path(self,path):
        if not os.path.isdir(path):
            os.mkdir(path)

    def notify(self,message):
        if self.verbose:
            print('LabJack: '+message) 

    def initialize_system(self):
        try:
            self.system = ljm.openS(self.model,self.connection,self.identifier)              
            self.notify('System initialized.')              
            self.loaded = True                                                   
            self.get_system_info()
            self.print_system_info()   
        except:
            self.system = None
            self.loaded = False                                     

    def get_system_info(self):
        self.info = dict()
        if self.loaded:
            info = ljm.getHandleInfo(self.system)
            self.info['device'] = info[0]
            self.info['connection'] = info[1]
            self.info['serial'] =  info[2]
            self.info['ip'] = ljm.numberToIP(info[3])
            self.info['port'] = info[4]
            self.info['bytemax'] = info[5]

    def print_system_info(self):
        if self.loaded:
            info = self.info
            self.notify("\nOpened a LabJack with Device type: %i, Connection type: %i,\n"
                        "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
                        (info['device'], info['connection'], info['serial'], info['ip'], info['port'], info['bytemax']))                                 

    def initialize_channel(self):
        if self.loaded:
            # set resolution and gain of analog channel
            ljm.eWriteName(self.system, self.channel+"_RESOLUTION_INDEX", self.resolution)
            ljm.eWriteName(self.system, self.channel+"_RANGE", self.range)

    def read_channel(self):
        data = []
        if self.loaded:
            data = ljm.eReadName(self.system, self.channel)
        return data

    def release(self):
        if self.loaded:
            ljm.close(self.system)

if __name__ == "__main__":
 
    # instantiate class
    daq = LabJack420Py()    
    
    # transmitter linear conversion parameters (pH from [-2.00, 16.00] is mapped sent as current from [4,20] mA)
    slope = 1125 # transmitted signal slope [mA/pH]
    offset = -6.5 # transmitted signal offset [pH]

    # prepare for logging
    timestamp = datetime.datetime.now() 
    timestampStr = timestamp.strftime("%Y/%m/%d %I:%M:%S%p")
    timestampName = timestamp.strftime("%Y_%m_%d-%I_%M_%S%p")
    filename = timestampName + "-%s.csv"%(channel)
    fullfilename = os.path.join(self.path['output'], filename)
    print("Start time is: %s" %(timestampStr))
    print("Reading %s %i times and saving data to the file:\n - %s\n" %(name, iterations, fullfilename))
    fileID = open(fullfilename, 'w')
    fileID.write("Time Stamp, Duration/Jitter [s], pH, Signal [V], Current [mA]\n") #" %(name))

    # intialize variables
    iterations = 10 
    duration = 0
    iteration = 0
    skips = 0
    interval = 0
    ljm.startInterval(interval, int(daq.rate))
    tic = ljm.getHostTick()

    # acquisition loop
    while iteration < iterations:
        try:
            # time
            skips = ljm.waitForNextInterval(interval)
            toc = ljm.getHostTick()
            duration = (toc-tic)
            time = datetime.datetime.now()
            timestamp = time.strftime("%Y/%m/%d %I:%M:%S%p")

            # reading
            voltage = daq.read_channel()
            current = voltage/resistance
            ph = slope*current+offset

            # Print values
            print("%s reading: pH of %f as %f V, duration: %0.1f ms, skipped intervals: %i" % (name, pH, voltage, duration, skips))
            fileID.write("%s, %0.1f, %0.3f, %0.3f, %0.3f\n" %(timestamp, duration, pH, voltage, current*1e3))
            tic = toc
            iteration = iteration + 1
        except KeyboardInterrupt:
            break
        except Exception:
            import sys
            print(sys.exc_info()[1])
            break
    print("\nFinished!")

    # close open objects
    fileID.close()
    ljm.cleanInterval(interval)
    self.release()

# -*- coding: utf-8 -*-
