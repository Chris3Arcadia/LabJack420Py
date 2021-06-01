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

