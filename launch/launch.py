from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='13324106_Carousel',
            executable='publisher_node',
            name='publisher_node',
            output='screen'
        ),
        Node(
            package='13324106_Carousel',
            executable='subscriber_node',
            name='subscriber_node',
            output='screen'
        ),
    ])
