#!/usr/bin/python

import rospy
from demo_pkg.msg import demo_msg



def send_msg():

    rospy.init_node('demo_message_node')

    greeting_msg = 'Hello ROS developer!'

    pub = rospy.Publisher('greeting_number', demo_msg, queue_size=10)

    rate = rospy.Rate(10)

    my_msg = demo_msg()

    while not rospy.is_shutdown():
        my_msg.number = 2021
        my_msg.greeting = greeting_msg
        rospy.loginfo('Node is sending message...')
        pub.publish(my_msg)
        rate.sleep()



if __name__ == "__main__":

    send_msg()
