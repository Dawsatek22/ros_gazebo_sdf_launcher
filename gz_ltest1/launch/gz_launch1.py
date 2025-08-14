from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    #ros_gz_sim_pkg_path = get_package_share_directory('ros_gz_sim')
    example_pkg_path = FindPackageShare('gz_ltest1')  # Replace with your own package name
    gz_launch_path = PathJoinSubstitution([example_pkg_path, 'launch', 'gz_launch1.py'])

    return LaunchDescription([
       
        SetEnvironmentVariable(
            'GZ_SIM_PLUGIN_PATH',
            PathJoinSubstitution([example_pkg_path, 'plugins'])
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_launch_path),
            launch_arguments={
                'gz_args': [PathJoinSubstitution([example_pkg_path, 'models/testbuild3.sdf'])],  # Replace with your own world file
                'on_exit_shutdown': 'True'
            }.items(),
        ),

    ])