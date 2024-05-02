# Meta Package
Name:           ros-jazzy-ros-core
Version:        0.10.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros_core and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros_core
Requires:       ros2-jazzy-ros_core-devel

Obsoletes: ros-jazzy-ros-core < 0.10.0-1

%description
A package to aggregate the packages required to use publish /
subscribe, services, generate messages and other core ROS concepts.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.10.0-1
- Update to latest release
