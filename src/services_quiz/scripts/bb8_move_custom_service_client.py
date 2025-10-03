#! /usr/bin/env python
import rospkg
import rospy

from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest
# from BB8CustomServiceMessage import side, repetitions

rospy.init_node('bb8_move_custom_service_client_node') # init node for client

rospy.wait_for_service('/move_bb8_in_square_custom') # wait for the service

print("im first")

move_bb8_in_square_custom_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage) # connect to serv

print("im here")
# from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
move_bb8_in_square_custom_request_object = BB8CustomServiceMessageRequest() # create an obj

print("im there")

result = move_bb8_in_square_custom_client(move_bb8_in_square_custom_request_object) # send connection

print(result)