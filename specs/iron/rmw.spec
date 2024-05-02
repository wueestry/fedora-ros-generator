# Meta Package
Name:           ros-iron-rmw
Version:        7.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rmw and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rmw
Requires:       ros2-iron-rmw-devel

Obsoletes: ros-iron-rmw < 7.1.0-1

%description
Contains the ROS middleware API.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.7.1.0-1
- Update to latest release
