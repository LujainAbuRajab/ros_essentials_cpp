# :turtle: **Motion Trajectories for Turtlesim**

This project involves developing a Python script to control the motion of the Turtlesim robot in ROS (Robot Operating System). Users can select from various predefined motion trajectories and provide specific parameters to guide the robot’s movements accordingly.

---

## :white_medium_square: **Features**
The system provides the following motion trajectory options:
1. Square: The turtle moves in a square path.
2. Triangle: The turtle draws an equilateral triangle.
3. Circular: The turtle moves in a circular path.
4. Spiral: The turtle moves in a spiral pattern.
5. Point to Point: The turtle navigates to a specific (x, y) destination from its current position.
6. Zigzag Motion: The turtle moves back and forth in a zigzag pattern using triangular paths.
7. Exit: Exit the program.

---

## :white_medium_square: **User Input**
The script prompts the user to select one of the motion trajectories and provides specific instructions based on the chosen trajectory:

### 1. Square Trajectory

+ Prompt: Enter the edge dimension of the square.
+ Action: The turtle will move in a square path with the specified edge length.
+ ![Square Trajectory](https://github.com/LujainAbuRajab/ros_essentials_cpp/blob/e07b61a8c109909340a00d37c85495a6d5d6be38/src/topic03_perception/images/Sq.png)

### 2. Triangle Trajectory

+ Prompt: Enter the length of the triangle’s side.
+ Action: The turtle will draw an equilateral triangle.
+ ![Triangle Trajectory](https://github.com/LujainAbuRajab/ros_essentials_cpp/blob/e07b61a8c109909340a00d37c85495a6d5d6be38/src/topic03_perception/images/tri.png)

### 3. Circular Trajectory

+ Prompt: Enter the radius of the circle.
+ Action: The turtle will move in a circular path with the given radius.
+ ![Circular Trajectory](https://github.com/LujainAbuRajab/ros_essentials_cpp/blob/e07b61a8c109909340a00d37c85495a6d5d6be38/src/topic03_perception/images/circ.png)

### 4. Spiral Trajectory

+ Prompt: Enter the change in radius for the spiral shape.
+ Action: The turtle will move in an expanding or contracting spiral based on the input.
+ ![Spiral Trajectory](https://github.com/LujainAbuRajab/ros_essentials_cpp/blob/e07b61a8c109909340a00d37c85495a6d5d6be38/src/topic03_perception/images/spir.png)

### 5. Point to Point Trajectory

+ Prompt: Enter the destination coordinates (x, y).
+ Action: The turtle will navigate from its current position to the specified destination.
+ ![Point to Point Trajectory](https://github.com/LujainAbuRajab/ros_essentials_cpp/blob/e07b61a8c109909340a00d37c85495a6d5d6be38/src/topic03_perception/images/line.png)

### 6. Zigzag Motion

+ Prompt: The system will prompt for required parameters to execute zigzag motio
+ Action: The turtle will navigate back and forth using triangular paths to create a zigzag pattern.
+ ![Zigzag Motion](https://github.com/LujainAbuRajab/ros_essentials_cpp/blob/e07b61a8c109909340a00d37c85495a6d5d6be38/src/topic03_perception/images/zig.png)

### 7. Exit

+ Action: Terminates the program.

---

## :white_medium_square: Prerequisites

+ ROS: Installed and configured on your system.
+ Turtlesim Package: Available in the ROS environment.
+ Python 3.x: Required to execute the script.

---
##  :white_medium_square: Setup

1. Clone the repository:
   
   ```bash

    cd turtlesim_motion_trajectory

    ```
2. Navigate to the project directory:
   
   ```bash

    cd turtlesim_motion_trajectory

    ```
3. Ensure the ROS environment is sourced:
    
   ```bash

    source /opt/ros/<ros_distro>/setup.bash
   
    ```
4. Run the Python script:
    
   ```bash

    python3 motion_trajectory.py

    ```
   
---

## :white_medium_square: How to Use

1. Launch the Turtlesim node in ROS:
   
   ```bash

    rosrun turtlesim turtlesim_node

    ```
2. Execute the Python script to interact with the trajectory system.
3. Follow the prompts to select a motion trajectory and provide the required parameters.

---
##  :white_medium_square:Example

  ```bash

    Select one of the following motion trajectories for turtle robot:
    1. Square
    2. Triangle
    3. Circular
    4. Spiral
    5. Point to Point
    6. Zigzag motion
    7. Exit
    Enter your choice (1-7): 3
    
    Enter the radius of the circle: 5

  ```
The turtle will then move in a circular trajectory with a radius of 5 units.

---
### Let me know if you need help with any specific part of this! 😊  

