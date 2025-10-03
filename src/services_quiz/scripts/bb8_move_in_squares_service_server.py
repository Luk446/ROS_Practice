#! /usr/bin/env python

# import packages and msgs 
import rospy
import math

# import movmnt pkg
from geometry_msgs.msg import Twist
# import custom srv msg
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse

def move_square(side_length, repetitions, linear_speed=0.2, angular_speed=0.5):
    move_time = side_length / linear_speed
    turn_time = (math.pi / 2) / angular_speed

    for rep in range(repetitions):
        rospy.loginfo(f"Square (side={side_length}m) Rep: {rep + 1}")
        for side in range(4):
            rospy.loginfo(f"Moving side {side + 1} of square (side={side_length}m)")
            # Move straight
            move_in_squares.linear.x = linear_speed
            move_in_squares.angular.z = 0.0
            my_pub.publish(move_in_squares)
            rospy.sleep(move_time)

            # Stop
            move_in_squares.linear.x = 0.0
            my_pub.publish(move_in_squares)
            rospy.sleep(0.5)

            # Turn 90 degrees
            move_in_squares.angular.z = angular_speed
            my_pub.publish(move_in_squares)
            rospy.sleep(turn_time)

            # Stop
            move_in_squares.angular.z = 0.0
            my_pub.publish(move_in_squares)
            rospy.sleep(0.5)

        rospy.loginfo("Finished one repetition of square")

    # Ensure stopped
    move_in_squares.linear.x = 0.0
    move_in_squares.angular.z = 0.0
    my_pub.publish(move_in_squares)


def my_callback(request):
    rospy.loginfo(f"Service request: side={request.side}m, repetitions={request.repetitions}")
    rospy.loginfo("The service bb8 move in squares has begun")

    # Move small square (side length 1.0, 2 repetitions)
    move_square(1.0, 2)

    rospy.loginfo("Small square movement finished")

    # Move large square (side length 2.0, 1 repetition)
    move_square(2.0, 1)

    rospy.loginfo("Large square movement finished")
    rospy.loginfo("Finished service bb8 move in squares")

    return BB8CustomServiceMessageResponse()

rospy.init_node('bb8_move_server')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_in_squares = Twist()

rate = rospy.Rate(10)
while not rospy.is_shutdown():
    rate.sleep()
