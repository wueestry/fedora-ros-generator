# Meta Package
Name:           ros-iron-ament-cmake-ros
Version:        0.11.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_cmake_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_cmake_ros
Requires:       ros2-iron-ament_cmake_ros-devel

Obsoletes: ros-iron-ament-cmake-ros < 0.11.2-1

%description
The ROS specific CMake bits in the ament buildsystem.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.11.2-1
- Update to latest release
