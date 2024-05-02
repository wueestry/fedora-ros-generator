# Meta Package
Name:           ros-jazzy-common-interfaces
Version:        5.3.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-common_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-common_interfaces
Requires:       ros2-jazzy-common_interfaces-devel

Obsoletes: ros-jazzy-common-interfaces < 5.3.5-1

%description
common_interfaces contains messages and services that are widely used
by other ROS packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.5-1
- Update to latest release
