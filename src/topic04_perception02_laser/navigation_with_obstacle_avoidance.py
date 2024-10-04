#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math
import time

# PID controller class
class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0
        self.last_time = None

    def compute(self, target, current):
        error = target - current
        current_time = time.time()
        delta_time = (current_time - self.last_time) if self.last_time else 0.1
        self.last_time = current_time

        # Proportional term
        P = self.Kp * error

        # Integral term
        self.integral += error * delta_time
        I = self.Ki * self.integral

        # Derivative term
        derivative = (error - self.prev_error) / delta_time if delta_time > 0 else 0
        D = self.Kd * derivative
        self.prev_error = error

        # Output of PID controller
        return P + I + D

class ObstacleAvoider:
    def __init__(self):
        rospy.init_node('pid_obstacle_avoider', anonymous=True)
        self.velocity_publisher = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=10)
        rospy.Subscriber("/scan", LaserScan, self.scan_callback)
        self.pid_linear = PID(Kp=0.5, Ki=0.0, Kd=0.1)  # PID for linear velocity
        self.pid_angular = PID(Kp=1.0, Ki=0.0, Kd=0.2)  # PID for angular velocity
        self.target_distance = 1.0  # Desired distance from obstacles
        self.front_distance = 9999
        self.left_distance = 9999
        self.right_distance = 9999
        self.angular_velocity = 0.0
        self.linear_velocity = 0.0

    def scan_callback(self, scan_data):
        # Divide the laser scan into three regions: left, front, and right
        num_ranges = len(scan_data.ranges)
        left_ranges = scan_data.ranges[:num_ranges // 3]
        front_ranges = scan_data.ranges[num_ranges // 3: 2 * num_ranges // 3]
        right_ranges = scan_data.ranges[2 * num_ranges // 3:]

        # Calculate the minimum distance in each region
        self.front_distance = self.get_min_distance(front_ranges)
        self.left_distance = self.get_min_distance(left_ranges)
        self.right_distance = self.get_min_distance(right_ranges)

    def get_min_distance(self, ranges):
        valid_ranges = [x for x in ranges if not math.isnan(x)]
        return min(valid_ranges) if len(valid_ranges) > 0 else 9999

    def move(self):
        rate = rospy.Rate(10)  # 10 Hz loop rate
        cmd_vel = Twist()

        while not rospy.is_shutdown():
            # Compute PID for linear velocity
            self.linear_velocity = self.pid_linear.compute(self.target_distance, self.front_distance)
            if self.front_distance < self.target_distance:
                # If an obstacle is too close, slow down
                self.linear_velocity = max(self.linear_velocity, 0.0)
            else:
                # Keep a moderate speed when clear
                self.linear_velocity = min(self.linear_velocity, 0.5)

            # Compute PID for angular velocity based on left and right distances
            if self.front_distance < self.target_distance:
                if self.left_distance < self.right_distance:
                    # Turn right if the left side is closer to an obstacle
                    self.angular_velocity = -self.pid_angular.compute(self.target_distance, self.left_distance)
                else:
                    # Turn left if the right side is closer to an obstacle
                    self.angular_velocity = self.pid_angular.compute(self.target_distance, self.right_distance)
            else:
                # Move straight if there are no obstacles in front
                self.angular_velocity = 0.0

            # Apply velocities to cmd_vel message
            cmd_vel.linear.x = self.linear_velocity
            cmd_vel.angular.z = self.angular_velocity
            self.velocity_publisher.publish(cmd_vel)

            rate.sleep()

if __name__ == '__main__':
    try:
        obstacle_avoider = ObstacleAvoider()
        time.sleep(2)  # Wait for the system to be ready
        obstacle_avoider.move()
    except rospy.ROSInterruptException:
        pass
