# Meta Package
Name:           ros-iron-fastrtps-cmake-module
Version:        3.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-fastrtps_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-fastrtps_cmake_module
Requires:       ros2-iron-fastrtps_cmake_module-devel

Obsoletes: ros-iron-fastrtps-cmake-module < 3.0.2-1

%description
Provide CMake module to find eProsima FastRTPS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.0.2-1
- Update to latest release
