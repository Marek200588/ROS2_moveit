import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    api_node = Node(
        package='moveit_fastapi_bridge',
        executable='api_server',
        name='fastapi_bridge_node',
        output='screen',
        emulate_tty=True
    )

    # 2. Twoje środowisko z MoveIt i RViz (z paczki ze screena)
    moveit_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('my_robot_moveit_config'),
                'launch',
                'demo.launch.py' 
            )
        )
    )

    # Uruchamiamy jedno i drugie równolegle
    return LaunchDescription([
        moveit_launch,
        api_node
    ])
