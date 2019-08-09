#!/usr/bin/env python
import rospy
import socket
from geometry_msgs.msg import Twist
def move():
    # Starts a new node
    rospy.init_node('iRobotMessageReceiver', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    # TCP config
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
    sock.bind(("10.154.116.54", 4002))

    while True:
        char, addr = sock.accept(1)
        if char == "right":
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = -2
            velocity_publisher.publish(vel_msg)
        elif char == "left":
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 2    
            velocity_publisher.publish(vel_msg) 
        elif char == "straight":
            vel_msg.linear.x = 0.1
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0     
            velocity_publisher.publish(vel_msg) 
        elif char == "back":
            vel_msg.linear.x = -0.1
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
        elif char == "stop": ## Stop
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    move()
