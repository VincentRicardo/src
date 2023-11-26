#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from time import sleep
from adafruit_servokit import ServoKit

#kaki kanan belakang
#Jalan state 1
#Berdiri state 0

#kit = ServoKit(channels=16)

# def berdiri():
#     kit.servo[9].angle = 55
#     sleep(1)
#     kit.servo[10].angle = 70
#     sleep(1)
#     kit.servo[11].angle = 0
#     sleep(1)
# def jalan():
#     kit.servo[11].angle = 90
#     sleep(1)
#     kit.servo[10].angle = 110
#     sleep(1)
#     kit.servo[9].angle = 110
#     sleep(1)
#     kit.servo[9].angle = 55
#     sleep(1)
#     kit.servo[10].angle = 70
#     sleep(1)
#     kit.servo[11].angle = 0
#     sleep(1)


class MyNode(Node):
    def __init__(self):
        super().__init__("kaki4_node")
        self.subscriber_message_ = self.create_subscription(String, "/state", self.repeat_, 1)
    
    def repeat_(self, message: String):
        if int(message.data)==0: #State berdiri
            self.get_logger().info("Menerima State Berdiri")
            #berdiri()
        if int(message.data)==1: #State Jalan
            self.get_logger().info("Menerima State Jalan")
            #jalan()
        if int(message.data)==2:
            self.get_logger().info("Menerima Informasi Dari Ultasonik")

def main(args=None):
    rclpy.init(args=args)
    #Code Berdiri
    #berdiri()
    #Code buat adjust
    #kit.servo[0].angle = 86
    #sleep(1)
    #kit.servo[1].angle = 90
    #sleep(1)
    #kit.servo[2].angle = 0
    #sleep(1)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()