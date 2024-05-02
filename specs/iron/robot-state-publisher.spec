# Meta Package
Name:           ros-iron-robot-state-publisher
Version:        3.2.1
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-robot_state_publisher and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-robot_state_publisher
Requires:       ros2-iron-robot_state_publisher-devel

Obsoletes: ros-iron-robot-state-publisher < 3.2.1-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.2.1-1
- Update to latest release
