#!/usr/bin/python

import rospy
from demo_pkg.msg import demo_msg

def callback_fun(msg):

    number_msg = msg.number
    greeting_msg = msg.greeting
    rospy.loginfo(f'{greeting_msg} , the recieved number is : {number_msg}')

def listener():

    rospy.init_node('demo_message_listener')

    subs = rospy.Subscriber('greeting_number', demo_msg, callback=callback_fun)



if __name__ == "__main__":

    while not rospy.is_shutdown():
        listener()