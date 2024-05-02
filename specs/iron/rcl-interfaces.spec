# Meta Package
Name:           ros-iron-rcl-interfaces
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rcl_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rcl_interfaces
Requires:       ros2-iron-rcl_interfaces-devel

Obsoletes: ros-iron-rcl-interfaces < 1.6.0-1

%description
The ROS client library common interfaces. This package contains the
messages and services which ROS client libraries will use under the
hood to communicate higher level concepts such as parameters.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.0-1
- Update to latest release
