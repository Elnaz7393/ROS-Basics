#!/usr/bin/python

import rospy
import sys
from demo_pkg.srv import demo_srv


def send_name(in_name):
    rospy.wait_for_service('greeting_service')

    client_greeting = rospy.ServiceProxy('greeting_service', demo_srv)

    response = client_greeting(in_name)

    print(f"Server responded ---> {response.out_greeting}")



if __name__ == "__main__":

    in_name = str(sys.argv[1])
    send_name(in_name)