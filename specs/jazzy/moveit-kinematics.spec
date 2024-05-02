# Meta Package
Name:           ros-jazzy-moveit-kinematics
Version:        2.9.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_kinematics and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_kinematics
Requires:       ros2-jazzy-moveit_kinematics-devel

Obsoletes: ros-jazzy-moveit-kinematics < 2.9.0-1

%description
Package for all inverse kinematics solvers in MoveIt

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
