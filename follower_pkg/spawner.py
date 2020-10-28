#! /usr/bin/python

import rospy
from turtlesim.srv import Spawn


rospy.init_node('turtle2_spawner_node')

rospy.wait_for_service('/spawn')
spawn_func = rospy.ServiceProxy('/spawn', Spawn)

turtle_name = rospy.get_param('~turtle2_name')
turtle2 = spawn_func(4.0, 4.0, 4.0, turtle_name)