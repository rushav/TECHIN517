- ros2 run usb_cam usb_cam_node_exe
- ros2 launch realsense2_camera rs_launch.py serial_no:="'349522071246'"
ros2 launch soa_bringup soa_bringup.launch.py

colcon build (inside ros2_ws)
source install/setup.bash

soa_params file in soa bring up/config

terminal 1: ros2 launch soa_bringup soa_bringup.launch.py display:=true
terminal 2: ros2 action send_goal /rosetta_client/run_policy \
    rosetta_interfaces/action/RunPolicy "{prompt: 'picking up an aruco cube and placing it in a yellow tray'}"
terminal 3: ros2 launch rosetta rosetta_client_launch.py contract_path:=/home/ubuntu/techin517/ros2_ws/src/soa_ros2/soa_bringup/rosetta_contracts/soa_act_contract.yaml
