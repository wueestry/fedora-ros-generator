# Meta Package
Name:           ros-jazzy-moveit-ros-planning-interface
Version:        2.12.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_ros_planning_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_ros_planning_interface
Requires:       ros2-jazzy-moveit_ros_planning_interface-devel

Obsoletes: ros-jazzy-moveit-ros-planning-interface < 2.12.2-1

%description
Components of MoveIt that offer simpler remote (as from another ROS 2
node) interfaces to planning and execution

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.12.2-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.12.1-1
- Update to latest release
* Thu Nov 21 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-2
- Rebuild due to srdfdom update
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
