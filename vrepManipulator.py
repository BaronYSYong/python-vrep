import vrep
import sys
import math

class Manipulator(object):
    def __init__(self, ip='127.0.0.1', port=19999, robot_name='UR3'):
        vrep.simxFinish(-1) # just in case, close all opened connections
        self.ID=vrep.simxStart(ip,port,True,True,5000,5) # Connect to V-REP
        if self.ID!=-1:
            print ('Connected to remote API server')
        else:
            print ('Failed connecting to remote API server')
            sys.exit('Could not connect')
        self.jointHandles = []
        for i in range(6):
            codeError, jointHandle = vrep.simxGetObjectHandle(self.ID, robot_name + '_joint' + str(i+1), vrep.simx_opmode_oneshot_wait)
            if codeError == 0:
                self.jointHandles.append(jointHandle)

    def MoveJoints(self, targetPos):
        for i in range(6):
            targetPos[i] = targetPos[i] * math.pi/180  
            
        for i in range(6):
            vrep.simxSetJointTargetPosition(self.ID, self.jointHandles[i], targetPos[i], vrep.simx_opmode_oneshot_wait)
                
    def ReadJoints(self):
        self.currentJointsPos = []
        for i in range(6):
            codeError, currentPos = vrep.simxGetJointPosition(self.ID, self.jointHandles[i], vrep.simx_opmode_oneshot_wait)
            if codeError == 0:
                self.currentJointsPos.append(currentPos* 180/math.pi)
        return self.currentJointsPos
    
    def GetJointInfo(self):
        obj_type_code = 1
        data_type_code = 16        
        code, handles, types_and_mode, limits_and_ranges, string_data = vrep.simxGetObjectGroupData(
            self.ID, obj_type_code, data_type_code, vrep.simx_opmode_oneshot_wait)
        print types_and_mode, limits_and_ranges


