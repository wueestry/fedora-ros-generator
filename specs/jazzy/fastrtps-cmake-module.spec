# Meta Package
Name:           ros-jazzy-fastrtps-cmake-module
Version:        3.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-fastrtps_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-fastrtps_cmake_module
Requires:       ros2-jazzy-fastrtps_cmake_module-devel

Obsoletes: ros-jazzy-fastrtps-cmake-module < 3.6.0-1

%description
Provide CMake module to find eProsima FastRTPS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.6.0-1
- Update to latest release
