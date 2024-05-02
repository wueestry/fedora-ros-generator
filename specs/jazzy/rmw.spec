# Meta Package
Name:           ros-jazzy-rmw
Version:        7.3.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw
Requires:       ros2-jazzy-rmw-devel

Obsoletes: ros-jazzy-rmw < 7.3.1-1

%description
Contains the ROS middleware API.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.7.3.1-1
- Update to latest release
