#!/usr/bin/python


import rospy
from std_msgs.msg import String
from demo_pkg.msg import demo_message


def callback_fun(msg):
    rospy.loginfo(msg.data)



if __name__=="__main__":
    rospy.init_node('subscriber_node')

    subs = rospy.Subscriber('/greeting', String, callback=callback_fun)
    rospy.spin()