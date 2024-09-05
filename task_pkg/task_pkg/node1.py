#!/usr/bin/env python3 
import rclpy 
from rclpy.node import Node 
import random
class my_node(Node):
    def __init__(self):
        super().__init__("node1")
        self.i=0
        self.nums = [random.randint(0, 100) for _ in range(12)]
        # Create a timer that calls the check() method every 1 second
        self.timer = self.create_timer(1.0, self.check)
    def check(self):
        if self.i < len(self.nums): 
            if self.nums[self.i] % 2 == 0: 
                self.get_logger().info(f"{self.nums[self.i]} is Even")
            else:
                self.get_logger().info(f"{self.nums[self.i]} is Odd")
            self.i += 1
        else:
            self.get_logger().info("No more numbers to check.")
            self.timer.cancel()
def main(args=None): 
    rclpy.init(args=args) 
    node = my_node()
    rclpy.spin(node) 
    rclpy.shutdown() 
if __name__ == "__main__": 
    main()