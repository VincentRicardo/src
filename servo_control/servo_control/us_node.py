#!/usr/bin/env python3
import rclpy
from time import sleep
import time
#import RPi.GPIO as GPIO
from rclpy.node import Node
from std_msgs.msg import String

# GPIO.setmode(GPIO.BCM)

# GPIO_TRIGGER = 18
# GPIO_ECHO = 24

# GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
# GPIO.setup(GPIO_ECHO, GPIO.IN)

# def distance():
#     GPIO.output(GPIO_TRIGGER, True)
#     sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)

#     StartTime = time.time()
#     StopTime = time.time()

#     while GPIO.input(GPIO_ECHO) == 0:
#         StartTime = time.time()
#     while GPIO.input(GPIO_ECHO)==1:
#         StartTime = time.time()
    
#     TimeElapsed = StopTime-StartTime

#     distance = (TimeElapsed*17150)

#     return distance

class MyNode(Node):
    def __init__(self):
        super().__init__("us_node")
        self.talking_one = self.create_publisher(String, "/state", 10)
        self.timer_ = self.create_timer(1, self.send_message)
    
    def send_message(self):
        message = String()
        message.data = str(15)
        #message.data = str(distance())
        self.get_logger().info("Jarak = " + message.data + " cm")
        #tambahin if kalo jarak deket = berdiri(state 0)/belok, kalo jauh jalan (state 1)
        self.talking_one.publish(message) #ini masih salah, bkn message yang dikirim
    
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()