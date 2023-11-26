#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__("jalan_node")
        self.talking_one = self.create_publisher(String, "/state", 1)
        message = String()
        message.data = str(1)
        self.get_logger().info("Mengirim State Jalan")
        self.talking_one.publish(message)
    
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.shutdown()