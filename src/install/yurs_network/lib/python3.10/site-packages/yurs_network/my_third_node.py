#!/usr/bin/env python3
from distutils.log import info
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__("Subscriber_2")
        self.subscription = self.create_subscription(
            String, 'topic', self.listener_callback, 10)
        self.subscription

    def listener_callback(self):
        self.get_logger(),info("Dogs!")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()