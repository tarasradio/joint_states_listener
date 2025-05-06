cmake_minimum_required(VERSION 2.8.3)
project(joint_states_listener)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation)

add_service_files(
  FILES
  ReturnJointStates.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy message_runtime
)
