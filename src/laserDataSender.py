#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import socket
import json
import yaml
import os

IP = os.environ.get("IPbaseDRI")

def convertToSend(data):
    data = yaml.load(str(data))
    data = json.dumps(data, indent=4)
    return data

def callback(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = convertToSend(msg)
    sock.sendto(data, (IP, 4001))
    
def listener():
    rospy.init_node('laserTransmiter', anonymous=True)

    rospy.Subscriber("scan", LaserScan, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()