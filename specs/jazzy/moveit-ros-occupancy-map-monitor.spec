# Meta Package
Name:           ros-jazzy-moveit-ros-occupancy-map-monitor
Version:        2.10.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_ros_occupancy_map_monitor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_ros_occupancy_map_monitor
Requires:       ros2-jazzy-moveit_ros_occupancy_map_monitor-devel

Obsoletes: ros-jazzy-moveit-ros-occupancy-map-monitor < 2.10.0-1

%description
Components of MoveIt connecting to occupancy map

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
