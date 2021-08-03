#!/usr/bin/python

import rospy
from std_msgs.msg import String

def talker():

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('takler', anonymous=True)
    rate = rospy.Rate(1) #Hz

    while not rospy.is_shutdown():
        message = "Hello, I'm Here. Can you here me? {}".format(rospy.get_time())
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()


if __name__ == '__main__':
    
    try:
        talker()
    except:
        pass