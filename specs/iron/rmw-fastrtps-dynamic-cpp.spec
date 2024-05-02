# Meta Package
Name:           ros-iron-rmw-fastrtps-dynamic-cpp
Version:        7.1.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rmw_fastrtps_dynamic_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rmw_fastrtps_dynamic_cpp
Requires:       ros2-iron-rmw_fastrtps_dynamic_cpp-devel

Obsoletes: ros-iron-rmw-fastrtps-dynamic-cpp < 7.1.3-1

%description
Implement the ROS middleware interface using introspection type
support.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.7.1.3-1
- Update to latest release
