# ROS 2 MoveIt & FastAPI Bridge 🤖⚡

A lightweight, asynchronous REST API bridge connecting modern web applications with ROS 2 and MoveIt 2. This package allows you to control a 6-DOF robotic arm and read its joint states in real-time via standard HTTP requests, completely abstracting the complexity of `ros2_control` and `sensor_msgs`.

## 🎯 Project Overview
Traditionally, controlling a robotic arm via ROS 2 requires native C++ or Python ROS nodes. This project introduces a **FastAPI-based middleware** that exposes the robot's hardware interface to any external client (Web Apps, Mobile Apps, or Cloud Services). 

### Key Features
* **Asynchronous Architecture:** Built on `rclpy` and `uvicorn`, ensuring non-blocking HTTP handling while maintaining the ROS 2 node spin loop in a background daemon thread.
* **Real-time Telemetry:** Instantaneous reading of joint states directly from hardware/encoders via the `/joint_states` topic.
* **Trajectory Execution:** Direct injection of `JointTrajectory` messages to the `ros2_control` trajectory controller.
* **Interactive Docs:** Auto-generated Swagger UI for instant API testing.

## 🛠️ Tech Stack
* **Robotics:** ROS 2 (Humble), MoveIt 2, URDF/Xacro
* **Backend:** Python 3.10+, FastAPI, Pydantic, Uvicorn
* **Communication:** RESTful HTTP, ROS 2 Pub/Sub

## 🚀 Quick Start

### 1. Build the Workspace
Ensure you have sourced your ROS 2 installation. Navigate to your workspace root and build the packages:
```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
### IN 3 awSEPARATE TERMINALS PASTE:
streamlit run ~/ros2_ws/src/my_robot_workspace/moveit_fastapi_bridge/moveit_fastapi_bridge/dashboard.py

ros2 run moveit_fastapi_bridge api_server

ros2 launch my_robot_moveit_config demo.launch.py

