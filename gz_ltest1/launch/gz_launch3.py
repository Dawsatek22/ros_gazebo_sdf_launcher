import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node

def generate_launch_description():

    # Setup project paths
   # pkg_project_bringup = get_package_share_directory('ros_gz_example_bringup')
    pkg_project_gazebo = get_package_share_directory('gz_ltest1')
    pkg_project_description = get_package_share_directory('gz_ltest1')
    pkg_ros_gz_sim = get_package_share_directory('gz_ltest1')

    # Load the SDF file from "description" package
    sdf_file  =  os.path.join(pkg_project_description, 'models', 'testbuild3.sdf')
    with open(sdf_file, 'r') as infp:
        robot_desc = infp.read()

    # Setup to launch the simulator and Gazebo world
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_launch3.py')), # is the launch command
        launch_arguments={'gz_args': PathJoinSubstitution([
            pkg_project_gazebo,
            'gz_ltest1',
            'src/gz_ltest1/models/testbuild3.sdf' # is the sdf file
        ])}.items(),
    )







    # Run the node
    return LaunchDescription([
        gz_sim,
    ])