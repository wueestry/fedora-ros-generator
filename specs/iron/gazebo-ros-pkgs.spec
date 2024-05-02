# Meta Package
Name:           ros-iron-gazebo-ros-pkgs
Version:        3.7.0
Release:        1%{?dist}
License:        BSD,LGPL,Apache 2.0
URL:            http://gazebosim.org/tutorials?cat=connect_ros
Summary:        Meta package for ros2-iron-gazebo_ros_pkgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-gazebo_ros_pkgs
Requires:       ros2-iron-gazebo_ros_pkgs-devel

Obsoletes: ros-iron-gazebo-ros-pkgs < 3.7.0-1

%description
Interface for using ROS with the

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.7.0-1
- Update to latest release
