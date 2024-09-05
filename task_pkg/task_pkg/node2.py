#!/usr/bin/env python3 
import rclpy 
from rclpy.node import Node 
import random
class my_node(Node):
    def __init__(self):
        super().__init__("node2")
        #collect data every 5 seconds
        self.timer=self.create_timer(5.0,self.collect_data)
    def collect_data(self):
        temperature = random.uniform(-10.0,50.0)
        pressure = random.uniform(900.0,1100.0)
        humidity=random.uniform(0.0,90.0)
        self.get_logger().info(f"Temperature : {temperature:.2f} Celsius , Pressure : {pressure:.2f} hPa , Humidity : {humidity :.2f} %")
def main(args=None): 
    rclpy.init(args=args) 
    node = my_node()
    rclpy.spin(node) 
    rclpy.shutdown() 
if __name__=="__main__":
    main()