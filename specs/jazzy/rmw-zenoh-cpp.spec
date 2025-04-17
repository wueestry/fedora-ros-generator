# Meta Package
Name:           ros-jazzy-rmw-zenoh-cpp
Version:        0.2.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw_zenoh_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw_zenoh_cpp
Requires:       ros2-jazzy-rmw_zenoh_cpp-devel

Obsoletes: ros-jazzy-rmw-zenoh-cpp < 0.2.3-1

%description
A ROS 2 middleware implementation using zenoh-cpp

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.2.3-1
- Update to latest release
* Sun Mar 02 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.2.2-1
- Update to latest release
