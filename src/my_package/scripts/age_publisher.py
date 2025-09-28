#! /usr/bin/env python3

import rospy
from my_package.msg import Age

rospy.init_node('publish_age_node')
pub = rospy.Publisher('/age_info', Age, queue_size=1)
rate = rospy.Rate(2)
age = Age()
age.years = 2
age.months = 4
age.days = 10

while not rospy.is_shutdown():
  pub.publish(age)
  rate.sleep()