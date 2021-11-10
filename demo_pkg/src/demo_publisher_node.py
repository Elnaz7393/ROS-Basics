#!/usr/bin/python

import rospy
from std_msgs.msg import String 




if __name__ == "__main__":

    rospy.init_node('publisher_node')

    pub = rospy.Publisher('greeting', String, queue_size=10)
    rate = rospy.Rate(10)

    greeting_msg = 'Hello there!'

    rospy.loginfo('Node is sending greeting ...')

    while(not(rospy.is_shutdown())):
        pub.publish(greeting_msg)
        rate.sleep()
    

