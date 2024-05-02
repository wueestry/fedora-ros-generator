# Meta Package
Name:           ros-iron-ros-industrial-cmake-boilerplate
Version:        0.4.0
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ros_industrial_cmake_boilerplate and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ros_industrial_cmake_boilerplate
Requires:       ros2-iron-ros_industrial_cmake_boilerplate-devel

Obsoletes: ros-iron-ros-industrial-cmake-boilerplate < 0.4.0-1

%description
Contains boilerplate cmake script, macros and utils

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.4.0-1
- Update to latest release
