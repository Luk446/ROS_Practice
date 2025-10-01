#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist


def my_callback(request):

    # call log
    rospy.loginfo("The Service move_bb8_in_circle has been called")

    #bb8 move chunk
    move_circle.linear.x = 0.2
    move_circle.angular.z = 0.2
    my_pub.publish(move_circle)
    rospy.loginfo("Finished service move_bb8_in_circle")

    # server response chunk
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

# init node
rospy.init_node('bb8_move_server') 

# create service
my_service = rospy.Service('/bb8_move_server', Empty, my_callback) # create the Service called my_service with the defined callback

# publish data to cmd_vel
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_circle = Twist()

rospy.spin() # maintain the service open.