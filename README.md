# Python Robot Simulation with V-Rep

## How to Start?
* Drag and drop 7 DoF Manipulator into screen
* Right click on redundantRobot and select Add -> Associated child script -> Threaded
* Open the script and print below to the script
```
simExtRemoteApiStart(19999)
```

### Terminal

* copy the necesarry files to working directory from V-REP python 
```
$ cp ~/V-REP_PRO_EDU_V3_4_0_Linux/programming/remoteApiBindings/python/python/* . 
```
* copy the share object from V-REP library
```
$ cp ~/V-REP_PRO_EDU_V3_4_0_Linux/programming/remoteApiBindings/lib/lib/64Bit/* .
```
* Test the server and client by runnning
```
$ python simpleTest.py
```

