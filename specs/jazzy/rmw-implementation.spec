# Meta Package
Name:           ros-jazzy-rmw-implementation
Version:        2.15.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw_implementation and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw_implementation
Requires:       ros2-jazzy-rmw_implementation-devel

Obsoletes: ros-jazzy-rmw-implementation < 2.15.5-1

%description
Proxy implementation of the ROS 2 Middleware Interface.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.15.5-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.15.4-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.15.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.15.2-1
- Update to latest release
