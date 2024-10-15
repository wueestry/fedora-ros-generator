# Meta Package
Name:           ros-humble-rmw-implementation
Version:        2.8.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rmw_implementation and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rmw_implementation
Requires:       ros2-humble-rmw_implementation-devel

Obsoletes: ros-humble-rmw-implementation < 2.8.4-1

%description
Proxy implementation of the ROS 2 Middleware Interface.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.8.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.8.3-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.8.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.8.2-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.8.2-1
- Initial humble build
