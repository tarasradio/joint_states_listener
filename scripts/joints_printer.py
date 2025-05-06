#!/usr/bin/env python

import roslib
roslib.load_manifest('joint_states_listener')
import rospy
from joint_states_listener.srv import ReturnJointStates
import time
import sys
import os

def call_return_joint_states(joint_names):
	rospy.wait_for_service("/ar600/return_joint_states")
	try:
		s = rospy.ServiceProxy("/ar600/return_joint_states", ReturnJointStates)
		resp = s(joint_names)
	except rospy.ServiceException:
		print ('error when calling return_joint_states')
		sys.exit(1)
	for (ind, joint_name) in enumerate(joint_names):
		if(not resp.found[ind]):
			print (")joint %s not found!"%joint_name)
	return (resp.position, resp.velocity, resp.effort)

# pretty-print list to string
def pplist(list):
  return ' '.join(['%2.3f'%x for x in list])

ns = 'ar600/'
joints = [ 'hip_f', 'hip_s', 'hip_r', 'knee', 'ankle_s', 'ankle_f' ] # r - yaw, f - pitch, s - roll

def get_joint_fullname(joint, side):
  return joint + '_joint_' + side

def getJointNames():
	joint_names = []
	for joint in joints:
		joint_names.append(get_joint_fullname(joint, 'left'))
		# joints.append(get_joint_fullname(joint, 'right'))
	return joint_names

def printJointStates():
	joint_names = getJointNames()

	while(1):
		(position, velocity, effort) = call_return_joint_states(joint_names)

		os.system('clear')
		print ('position:', pplist(position))
		print ('velocity:', pplist(velocity))
		print ('effort:', pplist(effort))

		time.sleep(0.1)

if __name__ == "__main__":
	try:
		printJointStates()
	except rospy.ROSInterruptException:
		pass