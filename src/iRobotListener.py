#!/usr/bin/env python
import rospy
import socket
from geometry_msgs.msg import Twist
def move():
    # Starts a new node
    rospy.init_node('iRobotMessageReceiver', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    # UDP config
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind(("192.168.1.68", 4002))

    while True:
        char, addr = sock.recvfrom(1024)
        if char == "right":
            print char
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = -2
            velocity_publisher.publish(vel_msg)
        elif char == "left":
            print char
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 2    
            velocity_publisher.publish(vel_msg) 
        elif char == "straight":
            print char
            vel_msg.linear.x = 0.2
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0     
            velocity_publisher.publish(vel_msg) 
        elif char == "back":
            print char
            vel_msg.linear.x = -0.2
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
        elif char == "stop": ## Stop
            print char
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    move()