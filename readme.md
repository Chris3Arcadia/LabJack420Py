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

If you run the class' `__main__` script, you will get the following output:

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
> Start time is: 2021/06/18 01:43:15PM
> 
> Reading AIN0 10 times and saving data to the file:
> 
> `C:\Users\ChrisArcadia\__temporary__\2021_06_18-01_43_15PM-AIN0.csv`
>
> AIN0 reading: pH of 3.645954 as -3.489676 V, duration: 100455.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of 3.704948 as -3.518485 V, duration: 100021.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of 3.679573 as -3.506093 V, duration: 100147.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of 3.668097 as -3.500489 V, duration: 99839.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of 3.644823 as -3.489123 V, duration: 100063.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of 3.631569 as -3.482651 V, duration: 99952.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of 3.605708 as -3.470022 V, duration: 100085.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of 3.700908 as -3.516512 V, duration: 99926.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of 3.697190 as -3.514696 V, duration: 100042.0 ms, skipped intervals: 0
> 
> AIN0 reading: pH of 3.676987 as -3.504830 V, duration: 100044.0 ms, skipped intervals: 0
>
> Finished!

