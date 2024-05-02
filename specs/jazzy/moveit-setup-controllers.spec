# Meta Package
Name:           ros-jazzy-moveit-setup-controllers
Version:        2.9.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-moveit_setup_controllers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_setup_controllers
Requires:       ros2-jazzy-moveit_setup_controllers-devel

Obsoletes: ros-jazzy-moveit-setup-controllers < 2.9.0-1

%description
MoveIt Setup Steps for ROS 2 Control

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
