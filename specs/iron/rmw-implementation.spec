# Meta Package
Name:           ros-iron-rmw-implementation
Version:        2.12.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rmw_implementation and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rmw_implementation
Requires:       ros2-iron-rmw_implementation-devel

Obsoletes: ros-iron-rmw-implementation < 2.12.0-1

%description
Proxy implementation of the ROS 2 Middleware Interface.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.12.0-1
- Update to latest release
