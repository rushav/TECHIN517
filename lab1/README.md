# Lab 1: Assemble SO101 Robot Arms

In this quarter, we will survey AI in robotics with robot arms.  
We will use the [SO101 arm](https://github.com/TheRobotStudio/SO-ARM100) to explore imitation learning, computer vision, and reinforcement learning.  
The first step is to assemble the arms and configure the working environment.  
By the end of this lab, you should have lerobot installed in conda on your host operating system, and ROS installed in a Docker devcontainer.


## Learning Objectives

- Assemble and calibrate a robot arm.
- Configure a Docker container to develop the arm with ROS.


## TODO

1. Collect a robot arm kit from the instructors.  
Fill out the included packing slip to confirm you recieved all necessary parts.  

2. Follow [Lerobot's installation instructions](https://huggingface.co/docs/lerobot/installation) to set up conda and the lerobot environment.  
Make sure you install miniconda in your home directory.  
I had to follow their troubleshooting guide to get everything to work.  
Install `'lerobot[all]'` instead of `pip install -e .` or `pip install lerobot`.

3. Follow the [instructions](https://huggingface.co/docs/lerobot/en/so101) to assemble, configure, and calibrate the arms.  
Use the name on the side of the robot for the calibration name.  

4. Fill out the partial [Dockerfile](/docker/INCOMPLETE_Dockerfile).  
Follow the `TODO` comments in the file.  
You should not need to modify the `devcontainer.json` or `setup.sh` files.  
Your `Dockerfile` should work with these other configurations to create a working dev environment.  
We will use a separate container to use Isaac Sim later.  


## Deliverables 

1. Return the packing slip that came with the kit with everyone's name to confirm you recieved all the necessary parts.  

2. Submit a video of you teleoperating the robot arm.  
You might need to wait on another team to finish assembling their leader / follower arm.  
Please be patient with the other team(s) and assemble your arm as soon as possible.

3. Submit your Dockerfile.

4. Submit a screenshot of the SO101 arm in Rviz2 in the Docker container.

5. Upload your arms calibration to the course Google Drive to share with the class.   
Any time you need to use a new arm, you should be able to download the calibration.  
If you need to update the calibration at any point, make sure to update the file in the drive as well. 


## FAQ

**Q:** My motors aren't working, why?  
**A:** You might need to update the motor's firmware.  
Refer to [the documentation](https://huggingface.co/docs/lerobot/feetech) for a guide on how to do so.  

**Q:** The motor position values jump when trying to calibrate the arm, then the arm jumps when teleoping the robot, why?  
**A:** Try calibrating the robot again, only move one joint at a time slowly.

**Q:** The calibration script says my motor's values are out of range, what do I do?  
**A:** You can use [this open-source software](https://github.com/CarolinePascal/FT_SCServo_Debug_Qt/tree/fix/port-search-timer) to check the firmware version of the motors.  
Make sure that all motors have the same version.  
If a motor has a different version, you will need a Windows computer to change the firmware.  
If all motors have the right firmware, try disconnecting and reconnecting the power and trying again.  
This might take many tries.  


## Resources

[Lychee AI Hub SO101 Arm Tutorials](https://lycheeai-hub.com/project-so-arm101-x-isaac-sim-x-isaac-lab-tutorial-series)  
Lychee AI is run by Muammer Bay, he partners with Nvidia to make high quality tutorials for ROS and Nvidia Isaac Sim.  
Also checkout his YouTube channel for more resources about AI in robotics.

[Georgia Institute of Technology ECE 4560](https://maegantucker.com/ECE4560/assignment1-so101/)  
This is another robotics course that utilizes the SO101 arm.  
Click through their labs and lectures for a different approach to these topics.

[Dockefile Keywords List](https://docs.docker.com/reference/dockerfile/)  
As you modify the given Dockerfile, checkout this list to see what the keywords do.  

[Docker for Robotics YouTube Playlist by Articulated Robotics](https://www.youtube.com/playlist?list=PLunhqkrRNRhaqt0UfFxxC_oj7jscss2qe)  
Environment management is extremely important for robotics development!  
We would run into infinitely more issues if all students installed these workspaces onto their own host machines.  
This lab requires you to modify a Dockerfile because understanding Docker genuinely makes development so much easier.  
