# Meta Package
Name:           ros-iron-common-interfaces
Version:        5.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-common_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-common_interfaces
Requires:       ros2-iron-common_interfaces-devel

Obsoletes: ros-iron-common-interfaces < 5.0.1-1

%description
common_interfaces contains messages and services that are widely used
by other ROS packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.5.0.1-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.5.0.0-1
- Update to latest release
