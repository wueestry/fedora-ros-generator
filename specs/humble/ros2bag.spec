# Meta Package
Name:           ros-humble-ros2bag
Version:        0.15.12
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ros2bag and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ros2bag
Requires:       ros2-humble-ros2bag-devel

Obsoletes: ros-humble-ros2bag < 0.15.12-1

%description
Entry point for rosbag in ROS 2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.12-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.11-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.9-1
- Update to latest release
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.8-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.7-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.7-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.7-1
- update to latest upstream
* Thu Jun 29 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.6-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.4-1
- Initial humble build
