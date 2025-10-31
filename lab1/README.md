# Lab 1: Assemble SO101 Robot Arms

In this quarter, we will survey AI in robotics with robot arms.  
We will use the [SO101 arm](https://github.com/TheRobotStudio/SO-ARM100) to explore imitation learning, computer vision, and reinforcement learning.  
The first step is to assemble the arms:


## Learning Objectives

- Assemble a robot arm.
- Configure a Docker container to develop the arm.


## TODO

1. Collect a robot arm kit from the instructors.

2. Fill out the partial [Dockerfile](/so101_ws/.devcontainer/Dockerfile)

3. Follow the [instructions](https://huggingface.co/docs/lerobot/en/so101) to assemble, configure, and calibrate the arms.


## Deliverables 

1. Submit your Dockerfile.

2. Submit a video of you teleoperating the robot arm from within your Docker container.  


## FAQ

**Q:** The motor position values jump when trying to calibrate the arm, then the arm jumps when teleoping the robot, why?  
**A:** Try calibrating the robot again, only move one joint at a time slowly.


## Resources

[Lychee AI Hub SO101 Arm Tutorials](https://lycheeai-hub.com/project-so-arm101-x-isaac-sim-x-isaac-lab-tutorial-series)  
Lychee AI is run by Muammer Bay, he partners with Nvidia to make high quality tutorials for ROS and Nvidia Isaac Sim.  
Also checkout his YouTube channel for more resources about AI in robotics.

[Georgia Institute of Technology ECE 4560](https://maegantucker.com/ECE4560/assignment1-so101/)  
This is another robotics course that utilizes the SO101 arm.  
Click through their labs and lectures for a different approach to these topics.
