# Meta Package
Name:           ros-iron-turtlebot3-gazebo
Version:        2.2.5
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://turtlebot3.robotis.com
Summary:        Meta package for ros2-iron-turtlebot3_gazebo and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-turtlebot3_gazebo
Requires:       ros2-iron-turtlebot3_gazebo-devel

Obsoletes: ros-iron-turtlebot3-gazebo < 2.2.5-1

%description
Gazebo simulation package for the TurtleBot3

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.2.5-1
- Update to latest release
