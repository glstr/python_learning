#! /bin/bash

if [ "$(uname)" != "Darwin" ];then
    echo "error system"
fi

# update brew and add ros denpendencies tap
brew tap ros/deps
brew tap osrf/simulation   # Gazebo, sdformat, and ogre
brew tap homebrew/core # VTK5
brew tap homebrew/science  # others
brew install pyqt5 --with-python

# setup environment 
mkdir -p ~/Library/Python/2.7/lib/python/site-packages
echo "$(brew --prefix)/lib/python2.7/site-packages" >> ~/Library/Python/2.7/lib/python/site-packages/homebrew.pth

# install some python tools
sudo -H python2 -m pip install -U wstool rosdep rosinstall rosinstall_generator rospkg catkin-pkg sphinx
rosdep update

# begin to build catkin packages
#create a catkin workspace
mkdir ~/ros_catkin_ws
cd ~/ros_catkin_ws

# desktop-full install
rosinstall_generator desktop_full --rosdistro kinetic --deps --wet-only --tar > kinetic-desktop-full-wet.rosinstall
wstool init -j8 src kinetic-desktop-full-wet.rosinstall

# resolving denpendencies
#rosdep install --from-paths src --ignore-src --rosdistro kinetic -y
rosdep install --from-paths src --ignore-src  --skip-keys google-mock --skip-keys python-wxtools --rosdistro kinetic -y

# building the catkin workspace
./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release
source ~/ros_catkin_ws/install_isolated/setup.bash





