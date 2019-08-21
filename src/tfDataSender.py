#!/usr/bin/env python
import rospy
from tf2_msgs.msg import TFMessage
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
    sock.sendto(data, (IP, 4004))
    
def listener():
    rospy.init_node('tfTransmiter', anonymous=True)

    rospy.Subscriber("tf", TFMessage, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()