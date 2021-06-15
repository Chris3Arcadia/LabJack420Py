# Read Me

This library provides a Python wrapper for reading 4-20mA signals using LabJack's T7 data logger.

By Chris Arcadia 

Created on 2021/05/30. 

## Software Requirements
* LabJack's [LJM driver](https://labjack.com/ljm) and [Python wrapper](https://labjack.com/support/software/examples/ljm/python) 
* [Python](https://www.python.org/getit) 2.6, 2.7 or 3.x** 

## Hardware Requirements

* LabJack [T7](https://labjack.com/products/t7) or [T4](https://labjack.com/products/t4) for reading the analog signals
* sensor that is transmitting the 4-20mA signals (such as a pH meter)
* CPU (Windows, macOS, or Linux) with USB 3 

## Environment Setup

1. get and install the [LJM Library](https://labjack.com/support/software/installers/ljm) (I installed [LabJack-2019-05-20.exe](https://labjack.com/sites/default/files/software/LabJack-2019-05-20.exe))
2. install the Python package [laback-ljm](https://pypi.org/project/labjack-ljm/) (using PIP: `pip install labjack-ljm`).
3. try running an example script (such as [simple_log.py](https://labjack.com/support/software/examples/ljm/python/additional-examples/simple-log) or one of the others on [GitHub](https://github.com/labjack/supplementary-ljm-examples/tree/master/python))

More detailed instructions can be found on LabJack's [Python for LJM](https://labjack.com/support/software/examples/ljm/python) page.

This library has been tested on a Windows device, but since the Python wrapper for LabJack works on Windows/Mac/Linux, this should work across platforms. The test setup was running Python 3.6.1 from [Anaconda 3](https://www.anaconda.com/)  (4.4.0).


## Example Output

If you run the class' "__main__" script, you will get the following output:

> LabJack: System initialized.
> 
> LabJack: 
> 
> Opened a LabJack with Device type: 7, Connection type: 1,
> 
> Serial number: 470014465, IP address: 0.0.0.0, Port: 0,
> 
> Max bytes per MB: 64
> 
> Start time is: 2021/06/15 05:21:21PM
> 
> Reading AIN0 10 times and saving data to the file:
> 
> `C:/Users/ChrisTow/Dropbox/INSPECT\__temporary__\2021_06_15-05_21_21PM-AIN0.csv`
>
> AIN0 reading: pH of -6.500799 as -0.000178 V, duration: 100519.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of -6.501154 as -0.000257 V, duration: 99561.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of -6.500799 as -0.000178 V, duration: 100447.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of -6.500799 as -0.000178 V, duration: 100007.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of -6.500799 as -0.000178 V, duration: 100020.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of -6.500799 as -0.000178 V, duration: 100015.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of -6.500799 as -0.000178 V, duration: 100004.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of -6.500799 as -0.000178 V, duration: 99954.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of -6.500799 as -0.000178 V, duration: 100046.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of -6.501154 as -0.000257 V, duration: 100003.0 ms, skipped intervals: 0
>
> Finished!

