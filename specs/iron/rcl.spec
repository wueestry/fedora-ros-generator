# Meta Package
Name:           ros-iron-rcl
Version:        6.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rcl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rcl
Requires:       ros2-iron-rcl-devel

Obsoletes: ros-iron-rcl < 6.0.5-1

%description
The ROS client library common implementation. This package contains an
API which builds on the ROS middleware API and is optionally built
upon by the other ROS client libraries.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.6.0.5-1
- Update to latest release
