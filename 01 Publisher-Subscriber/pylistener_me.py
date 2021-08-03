#!/usr/bin/python

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'yes I can hear U : %s ', data.data)


def listener():
    rospy.init_node('listener')
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except:
        pass
