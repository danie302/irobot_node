#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
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
    print data
    sock.sendto(data, ("192.168.1.65", 4003))
    
def listener():
    rospy.init_node('odomTransmiter', anonymous=True)

    rospy.Subscriber("odom", LaserScan, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()