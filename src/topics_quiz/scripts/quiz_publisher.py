#! /usr/bin/env python3

# import packages
import rospy # ignore: import-error
from geometry_msgs.msg import Twist # ignore: import-error
from sensor_msgs.msg import LaserScan # ignore: import-error

# global var for scan data
latest_scan = None

# data handling
def callback(msg):
    global latest_scan
    latest_scan = msg.ranges

# init nodes
rospy.init_node('topic_handler')

# communicate on nodes
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)

# def frequency
rate = rospy.Rate(2)

# def vel
vel = Twist()

while not rospy.is_shutdown():
    if latest_scan is not None:
        # Get the number of laser readings
        num_readings = len(latest_scan)
        
        # Get front reading (middle of the array)
        front_index = num_readings // 2
        front_distance = latest_scan[front_index]
        
        # Get left side reading (end of array - 180 degrees scope)
        left_index = num_readings - 1
        left_distance = latest_scan[left_index]
        
        # Get right side reading (beginning of array - 180 degrees scope)
        right_index = 0
        right_distance = latest_scan[right_index]
        
        # Reset velocities
        vel.linear.x = 0.0
        vel.angular.z = 0.0
        
        # Apply the logic rules
        # Rule 1: If front > 1m, move forward
        if front_distance > 1.0:
            vel.linear.x = 0.3  # Move forward
            
        # Rule 2: If front < 1m, turn left
        if front_distance < 1.0:
            vel.angular.z = 0.5  # Turn left
            
        # Rule 3: If right side < 1m, turn left
        if right_distance < 1.0:
            vel.angular.z = 0.5  # Turn left
            
        # Rule 4: If left side < 1m, turn right
        if left_distance < 1.0:
            vel.angular.z = -0.5  # Turn right
        
        # Publish the velocity command
        pub.publish(vel)
        
        # Debug output
        rospy.loginfo(f"Front: {front_distance:.2f}m, Left: {left_distance:.2f}m, Right: {right_distance:.2f}m")
    
    rate.sleep()