# Meta Package
Name:           ros-iron-ament-cmake-auto
Version:        2.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_cmake_auto and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_cmake_auto
Requires:       ros2-iron-ament_cmake_auto-devel

Obsoletes: ros-iron-ament-cmake-auto < 2.0.5-1

%description
The auto-magic functions for ease to use of the ament buildsystem in
CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.5-1
- Update to latest release
