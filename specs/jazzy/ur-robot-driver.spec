# Meta Package
Name:           ros-jazzy-ur-robot-driver
Version:        3.2.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ur_robot_driver and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ur_robot_driver
Requires:       ros2-jazzy-ur_robot_driver-devel

Obsoletes: ros-jazzy-ur-robot-driver < 3.2.0-1

%description
The new driver for Universal Robots UR3, UR5 and UR10 robots with CB3
controllers and the e-series.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.2.0-1
- Update to latest release
