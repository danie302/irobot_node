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
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = convertToSend(msg)
    sock.connect(("10.154.116.42", 4001))
    sock.send(data)
    sock.close()
    
def listener():
    rospy.init_node('laserTransmiter', anonymous=True)

    rospy.Subscriber("scan", LaserScan, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
