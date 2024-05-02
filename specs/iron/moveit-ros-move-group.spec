# Meta Package
Name:           ros-iron-moveit-ros-move-group
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-iron-moveit_ros_move_group and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_ros_move_group
Requires:       ros2-iron-moveit_ros_move_group-devel

Obsoletes: ros-iron-moveit-ros-move-group < 2.8.0-1

%description
The move_group node for MoveIt

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
