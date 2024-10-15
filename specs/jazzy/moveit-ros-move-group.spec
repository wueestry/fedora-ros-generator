# Meta Package
Name:           ros-jazzy-moveit-ros-move-group
Version:        2.10.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_ros_move_group and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_ros_move_group
Requires:       ros2-jazzy-moveit_ros_move_group-devel

Obsoletes: ros-jazzy-moveit-ros-move-group < 2.10.0-1

%description
The move_group node for MoveIt

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
