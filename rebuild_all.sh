#! etc/bin/bash

./ros_generator.py -b -o wueestry -p ros --chroot $1 desktop desktop_full mavros moveit joy ackermann_msgs -r -D noetic -c "Update all packages"
./ros_generator.py -b -o wueestry -p ros --chroot $1 desktop -r -D humble -c "Update all packages"