ARG CUDA_VERSION=12.4.1
ARG OS_VERSION=22.04

### build image ###
FROM nvidia/cuda:${CUDA_VERSION}-base-ubuntu${OS_VERSION} AS build

RUN echo 'Acquire::Retries "3";' > /etc/apt/apt.conf.d/80retries

# Add the official OSRF ROS 2 apt repository and install ROS Humble Desktop
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gnupg2 \
    lsb-release \
    software-properties-common \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
       -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu jammy main" \
       | tee /etc/apt/sources.list.d/ros2.list > /dev/null \
    && apt-get update && apt-get install -y --no-install-recommends \
    ros-humble-desktop \
    && rm -rf /var/lib/apt/lists/*

# Install python3-pip and python-is-python3 so "python" invokes Python 3
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python-is-python3 \
    && rm -rf /var/lib/apt/lists/*

# Install lerobot with feetech motor support for the SO-101 arm
RUN pip install --no-cache-dir 'lerobot[feetech]'

# Install Intel RealSense Python SDK for depth camera support
RUN pip install --no-cache-dir pyrealsense2


### dev ###
# It's common to separate images for different purposes (build, dev, runtime).
# You can do this with:
#   - multiple Dockerfiles, each building its own image, or
#   - a single Dockerfile with multiple build stages (multiple FROM lines)
#     then choose which stage to build using `--target`
# This stage reuses everything from the `build` stage and adds dev tools
FROM build AS dev

# Create non-root "ubuntu" user with passwordless sudo
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -s /bin/bash -G sudo ubuntu \
    && echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu

# general dev tools
RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    vim \
    nano \
    less \
    tmux

# environment settings in the bashrc
RUN echo "export PATH=\"$HOME/.local/bin:$PATH\"" >> /home/ubuntu/.bashrc && \
    echo "source /opt/ros/humble/setup.bash" >> /home/ubuntu/.bashrc  && \
    echo "source /home/ubuntu/techin517/ros2_ws/install/setup.bash" >> /home/ubuntu/.bashrc && \
    echo "export ROS_LOCALHOST_ONLY=1" >> /home/ubuntu/.bashrc && \
    echo "export HF_USER=ubuntu" >> /home/ubuntu/.bashrc && \
    echo "export XDG_RUNTIME_DIR=/tmp/runtime-ubuntu" >> /home/ubuntu/.bashrc

# Default shell
CMD ["/bin/bash"]
