# Meta Package
Name:           ros-jazzy-rcl
Version:        9.2.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcl
Requires:       ros2-jazzy-rcl-devel

Obsoletes: ros-jazzy-rcl < 9.2.3-1

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
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.2-1
- Update to latest release
