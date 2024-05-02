# Meta Package
Name:           ros-jazzy-robot-state-publisher
Version:        3.3.3
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-robot_state_publisher and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-robot_state_publisher
Requires:       ros2-jazzy-robot_state_publisher-devel

Obsoletes: ros-jazzy-robot-state-publisher < 3.3.3-1

%description
This package take the joint angles of a robot as input, and publishes
the 3D poses of the robot links to tf2, using a kinematic tree model
of the robot.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.3.3-1
- Update to latest release
