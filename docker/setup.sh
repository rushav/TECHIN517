source /home/ubuntu/.bashrc
cd /home/ubuntu/techin517/third_party/lerobot
pip install 'lerobot[all]'
cd /home/ubuntu/techin517/so101_ws/src/so101_ros2/
bash build.sh
ln -s $LEROBOT_SRC $SO101BRIDGE_INSTALL_SITE_PACKAGES
source /home/ubuntu/.bashrc
