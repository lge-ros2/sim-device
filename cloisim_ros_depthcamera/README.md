# CLOiSim-ROS Depth Camera

support ros remapping, --ros-args -r /test:=test

```shell
ros2 run cloisim_ros_depthcamera standalone
```

or

```shell
ros2 run cloisim_ros_depthcamera standalone --ros-args -p single_mode:=True -p target_model:=cloi1 -p target_parts_name:=depthcamera
```

or

```shell
ros2 run cloisim_ros_depthcamera standalone --ros-args -p target_model:=cloi1 -p target_parts_name:=depthcamera
```
