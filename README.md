# Python Robot Simulation with V-Rep

## Environment
* Ubuntu 16.04 Xenial
* V-REP_PRO_EDU_V3_4_0_Linux
    * downlaod from http://www.coppeliarobotics.com/downloads.html
    * axel http://coppeliarobotics.com/files/V-REP_PRO_EDU_V3_4_0_Linux.tar.gz

## Reference
* http://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm
* vrep-api-python 0.1.0
* http://teaching-robotics.org/trs2014/data/renaud.pdf
* https://www.youtube.com/watch?v=OfpB87pRoUk

## How to Start?
### V-REP
* Drag and drop UR3 into screen
* Right click on redundantRobot and select Add -> Associated child script -> Threaded
* Open the script and print below to the script
```
simExtRemoteApiStart(19999)
```
* Start the simulation

### Terminal
* clone this repository
```
$ cd ~/github
$ git clone https://github.com/BaronYSYong/python-vrep.git
$ cd python-vrep
```
* copy the necesarry files to working directory from V-REP python 
```
$ cp ~/V-REP_PRO_EDU_V3_4_0_Linux/programming/remoteApiBindings/python/python/* . 
```
* copy the share object from V-REP library (If your V-Rep is 64 bits)
```
$ cp ~/V-REP_PRO_EDU_V3_4_0_Linux/programming/remoteApiBindings/lib/lib/64Bit/* .
```
* Test the server and client by runnning
```
$ python simpleTest.py
```
* If the connection is OK, next try
```
$ ipython -i vrepManipulator.py
```
In IPython, try command below:
```
>>> UR = Manipulator()
>>> UR.MoveJoints([0,0,0,0,90,0])
>>> UR.ReadJoints()
>>> UR.GetJointInfo()
>>> LBR = Manipulator(robot_name='LBR_iiwa_14_R820')
>>> LBR.MoveJoints([45,90,90,45,90,0])
```



