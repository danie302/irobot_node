#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
import socket
import json
import yaml

def convertToSend(data):
    data = yaml.load(str(data))
    data = json.dumps(data, indent=4)
    return data

def callback(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = convertToSend(msg)
    sock.sendto(data, ("192.168.0.3", 4003))
    
def listener():
    rospy.init_node('odomTransmiter', anonymous=True)

    rospy.Subscriber("odom", Odometry, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()