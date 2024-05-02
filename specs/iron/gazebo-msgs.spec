# Meta Package
Name:           ros-iron-gazebo-msgs
Version:        3.7.0
Release:        1%{?dist}
License:        BSD
URL:            http://gazebosim.org/tutorials?cat=connect_ros
Summary:        Meta package for ros2-iron-gazebo_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-gazebo_msgs
Requires:       ros2-iron-gazebo_msgs-devel

Obsoletes: ros-iron-gazebo-msgs < 3.7.0-1

%description
Message and service data structures for interacting with Gazebo from
ROS2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.7.0-1
- Update to latest release
