#!/usr/bin/python

import rospy
from demo_pkg.srv import demo_srv


def say_hello(req):

    resp = 'Hello dear ' + '"' + req.in_name + '"'

    print(resp)

    return (resp)
    

def say_hello_server():
    rospy.init_node("demo_service_server")

    server = rospy.Service('greeting_service', demo_srv, handler=say_hello)
    print("Server is ready to say greeting :)")
    rospy.spin()


if __name__ == "__main__":

    say_hello_server()