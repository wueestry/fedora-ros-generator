# Meta Package
Name:           ros-iron-launch-testing-ros
Version:        0.24.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-launch_testing_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-launch_testing_ros
Requires:       ros2-iron-launch_testing_ros-devel

Obsoletes: ros-iron-launch-testing-ros < 0.24.1-1

%description
A package providing utilities for writing ROS2 enabled launch tests.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.24.1-1
- Update to latest release
