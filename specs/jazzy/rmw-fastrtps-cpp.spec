# Meta Package
Name:           ros-jazzy-rmw-fastrtps-cpp
Version:        8.4.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw_fastrtps_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw_fastrtps_cpp
Requires:       ros2-jazzy-rmw_fastrtps_cpp-devel

Obsoletes: ros-jazzy-rmw-fastrtps-cpp < 8.4.0-1

%description
Implement the ROS middleware interface using eProsima FastRTPS static
code generation in C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.8.4.0-1
- Update to latest release
