# Meta Package
Name:           ros-humble-map-msgs
Version:        2.1.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/map_msgs
Summary:        Meta package for ros2-humble-map_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-map_msgs
Requires:       ros2-humble-map_msgs-devel

Obsoletes: ros-humble-map-msgs < 2.1.0-1

%description
This package defines messages commonly used in mapping packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.14.1-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.0-1
- Initial humble build
