# Meta Package
Name:           ros-jazzy-rcl-interfaces
Version:        2.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcl_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcl_interfaces
Requires:       ros2-jazzy-rcl_interfaces-devel

Obsoletes: ros-jazzy-rcl-interfaces < 2.0.2-1

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
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.2-1
- Update to latest release
