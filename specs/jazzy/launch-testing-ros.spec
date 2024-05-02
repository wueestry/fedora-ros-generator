# Meta Package
Name:           ros-jazzy-launch-testing-ros
Version:        0.26.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-launch_testing_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-launch_testing_ros
Requires:       ros2-jazzy-launch_testing_ros-devel

Obsoletes: ros-jazzy-launch-testing-ros < 0.26.5-1

%description
A package providing utilities for writing ROS2 enabled launch tests.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.5-1
- Update to latest release
