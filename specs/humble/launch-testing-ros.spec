# Meta Package
Name:           ros-humble-launch-testing-ros
Version:        0.19.7
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-launch_testing_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-launch_testing_ros
Requires:       ros2-humble-launch_testing_ros-devel

Obsoletes: ros-humble-launch-testing-ros < 0.19.7-1

%description
A package providing utilities for writing ROS2 enabled launch tests.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.7-1
- Update to latest release
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.6-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.5-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.5-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.4-1
- Initial humble build
