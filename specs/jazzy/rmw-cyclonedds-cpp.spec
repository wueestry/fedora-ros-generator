# Meta Package
Name:           ros-jazzy-rmw-cyclonedds-cpp
Version:        2.2.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw_cyclonedds_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw_cyclonedds_cpp
Requires:       ros2-jazzy-rmw_cyclonedds_cpp-devel

Obsoletes: ros-jazzy-rmw-cyclonedds-cpp < 2.2.1-1

%description
Implement the ROS middleware interface using Eclipse CycloneDDS in
C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.2.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.2.0-1
- Update to latest release
