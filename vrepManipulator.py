import vrep
import sys
import math

vrep.simxFinish(-1) # just in case, close all opened connections

clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP

if clientID!=-1:
    print ('Connected to remote API server')

else:
    print ('Failed connecting to remote API server')
    sys.exit('Could not connect')
    
jointHandles = []

for i in range(6):
    codeError, jointHandle = vrep.simxGetObjectHandle(clientID, 'UR3_joint' + str(i+1), vrep.simx_opmode_oneshot_wait)
    if codeError == 0:
        jointHandles.append(jointHandle)



currentJointsPos = []
for i in range(6):
    codeError, currentPos = vrep.simxGetJointPosition(clientID, jointHandles[i], vrep.simx_opmode_oneshot_wait)
    if codeError == 0:
        currentJointsPos.append(currentPos* 180/math.pi)

print currentJointsPos
    
targetPos1=[90,0,-0,0,0,0]

for i in range(6):
    targetPos1[i] = targetPos1[i] * math.pi/180  
    
for i in range(6):
    vrep.simxSetJointTargetPosition(clientID, jointHandles[i], targetPos1[i], vrep.simx_opmode_oneshot_wait)

currentJointsPos = []
for i in range(6):
    codeError, currentPos = vrep.simxGetJointPosition(clientID, jointHandles[i], vrep.simx_opmode_oneshot_wait)
    if codeError == 0:
        currentJointsPos.append(currentPos* 180/math.pi)

print currentJointsPos
