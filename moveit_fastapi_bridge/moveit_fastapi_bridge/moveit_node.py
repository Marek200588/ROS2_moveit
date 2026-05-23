from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration
from sensor_msgs.msg import JointState  # ZABRAKŁO IMPORTU

class MoveItSceneNode(Node):
    def __init__(self):
        super().__init__("fastapi_moveit_node")
        self.publisher = self.create_publisher(JointTrajectory, "/arm_controller/joint_trajectory", 10)
        self.get_logger().info("MoveItSceneNode has been started")
        self.current_joints = {}
        
        # W rclpy przyjęło się podawać te argumenty pozycyjnie bez nazywania
        self.create_subscription(JointState, "/joint_states", self.joint_state_callback, 10)
    
    def move_joints(self, joint_names:list[str], joint_positions:list[float], duration:float):
        try:
            msg = JointTrajectory()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.joint_names = joint_names
            
            point = JointTrajectoryPoint()
            # Pamiętaj o zabezpieczeniu na float!
            point.positions = [float(p) for p in joint_positions]
            
            point.time_from_start.sec = int(duration)
            point.time_from_start.nanosec = int((duration - int(duration)) * 1e9)
            
            msg.points = [point]
            self.publisher.publish(msg)
            return True
        except Exception as e:
            self.get_logger().error(f"Error occurred while moving joints: {e}")
            return False
        
    def joint_state_callback(self, msg):
        # Zamieniamy dwie listy z wiadomości ROS 2 bezpośrednio na słownik
        self.current_joints = dict(zip(msg.name, msg.position))