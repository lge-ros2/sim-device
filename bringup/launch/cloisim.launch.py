#
# LGE Advanced Robotics Laboratory
# Copyright (c) 2020 LG Electronics Inc., LTD., Seoul, Korea
# All Rights are Reserved.
#
# SPDX-License-Identifier: MIT
#
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import SetEnvironmentVariable
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration


def generate_launch_description() -> LaunchDescription:

    sim_path = LaunchConfiguration('sim_path')
    world = LaunchConfiguration('world')

    execute_multi_robot_simulator = ExecuteProcess(
        cmd=['./CLOiSim.x86_64', '-worldFile', world],
        cwd=[sim_path],
        output='screen')

    # Create environment variables
    stdout_linebuf_envvar = SetEnvironmentVariable(
        'RCUTILS_LOGGING_BUFFERED_STREAM', '1')

    declare_launch_argument_sim_path = DeclareLaunchArgument(
        'sim_path',
        default_value='',
        description='path where the CLOiSim simulator located')

    declare_launch_argument_world = DeclareLaunchArgument(
        'world',
        default_value='',
        description='It is World file name. Please check environments before run. [CLOISIM_WORLD_PATH, CLOISIM_MODEL_PATH]')

    # Create the launch description and populate
    ld = LaunchDescription()

    # Set environment variables
    ld.add_action(stdout_linebuf_envvar)

    # Add the actions to launch all nodes
    ld.add_action(declare_launch_argument_sim_path)
    ld.add_action(declare_launch_argument_world)
    ld.add_action(execute_multi_robot_simulator)

    return ld
