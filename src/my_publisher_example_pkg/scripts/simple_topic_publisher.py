#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
# count = Int32()
vel = Twist()
vel.linear.x = 0.5
vel.linear.z = 0.5

while not rospy.is_shutdown(): 
  pub.publish(vel)
  rate.sleep()