#! /usr/bin/python

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class follower:
	def __init__(self):
		self.pose = Pose()
		self.pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=1)
		self.pose_sub_1 = rospy.Subscriber('/turtle1/pose', Pose, self.follow)
		self.pose_sub_2 = rospy.Subscriber('/turtle2/pose', Pose, self.updatePose)

	def updatePose(self, newPose):
		self.pose = newPose

	def calculateTwist(self, pose1, pose2):
		res = Twist()
		angle = math.atan2(pose1.y - pose2.y, pose1.x - pose2.x)
		res.angular.z = angle - pose2.theta
		res.linear.x = pose1.linear_velocity
		return res

	def follow(self, turtle1Pose):
		msg = self.calculateTwist(turtle1Pose, self.pose)
		self.pub.publish(msg)

rospy.init_node('my_listener')

f = follower()

rospy.spin()
