#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber1(Node):

    def __init__(self):
        super().__init__("Subscriber_1")
        self.Subscriber_1 = self.create_subscription(
            String, 'topic', self.listener_callback, 10)

    def listener_callback(self):
        self.get_logger().info("Cats!")

def main(args=None):
    rclpy.init(args=args)
    node = Subscriber1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()