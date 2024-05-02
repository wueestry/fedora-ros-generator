# Meta Package
Name:           ros-jazzy-ament-cmake-ros
Version:        0.12.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_ros
Requires:       ros2-jazzy-ament_cmake_ros-devel

Obsoletes: ros-jazzy-ament-cmake-ros < 0.12.0-1

%description
The ROS specific CMake bits in the ament buildsystem.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.12.0-1
- Update to latest release
