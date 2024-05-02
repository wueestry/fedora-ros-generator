# Meta Package
Name:           ros-jazzy-webots-ros2-turtlebot
Version:        2023.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-jazzy-webots_ros2_turtlebot and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-webots_ros2_turtlebot
Requires:       ros2-jazzy-webots_ros2_turtlebot-devel

Obsoletes: ros-jazzy-webots-ros2-turtlebot < 2023.1.2-1

%description
TurtleBot3 Burger robot ROS2 interface for Webots.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2023.1.2-1
- Update to latest release
