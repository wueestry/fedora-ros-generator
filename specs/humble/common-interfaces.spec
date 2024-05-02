# Meta Package
Name:           ros-humble-common-interfaces
Version:        4.2.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-common_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-common_interfaces
Requires:       ros2-humble-common_interfaces-devel

Obsoletes: ros-humble-common-interfaces < 4.2.3-1

%description
common_interfaces contains messages and services that are widely used
by other ROS packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- Initial humble build
