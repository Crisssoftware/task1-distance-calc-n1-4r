#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float64
from math import sqrt

class PoseNode(Node):
    def __init__(self):
        super().__init__("pose_node")
        self.get_logger().info("Pose Node has launched successfully.")
        self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.pose_publisher =  self.create_publisher(Float64, "/turtle1/distance_from_origin", 10)
    
    def pose_callback(self, pose:Pose):
        dist = Float64()
        dist.data = sqrt((pose.x)**2 + (pose.y)**2)
        self.pose_publisher.publish(dist)        


def main(args = None):
    rclpy.init(args = args)
    dodge = PoseNode()
    rclpy.spin(dodge)
    rclpy.shutdown()