import vrep
import sys
import math
from prettytable import PrettyTable

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
        '''
        Reference
        http://www.coppeliarobotics.com/helpFiles/en/jointDescription.htm
        '''
        joint_mode = ['nth', 'Passive', 'IK', 'Dependent', 'Motion', 'Torque/force']
        joint_type = {10: 'Revolute', 11: 'Prismatic'}
        obj_type_code = 1
        '''
        data_type = 0: 
        retrieves the object names (in stringData.)
        '''
        code, handles, a, b, obj_name = vrep.simxGetObjectGroupData(
            self.ID, obj_type_code, 0, vrep.simx_opmode_oneshot_wait)           
        '''data_type = 16: 
        retrieves joint properties data 
        (in intData (2 values): joint type, joint mode (bit16=hybid operation). 
        In floatData (2 values): joint limit low, joint range (-1.0 if joint is cyclic))
        '''     
        code, handles, types_and_mode, limits_and_ranges, string_data = vrep.simxGetObjectGroupData(
            self.ID, obj_type_code, 16, vrep.simx_opmode_oneshot_wait)
        types = [types_and_mode[x] for x in range(0, len(types_and_mode),2)]
        mode = [types_and_mode[x] for x in range(1, len(types_and_mode),2)]
        lower_limit = [limits_and_ranges[x] for x in range(0, len(limits_and_ranges),2)]
        upper_limit = [limits_and_ranges[x] for x in range(1, len(limits_and_ranges),2)]
        t = PrettyTable(['Object Name', 'Joint Types', 'Joint Modes', 'Lower Limit', 'Upper Limit'])
        for i in range(len(obj_name)):              
            t.add_row([obj_name[i], joint_type[types[i]], joint_mode[mode[i]], lower_limit[i], upper_limit[i]])  
        print t  


