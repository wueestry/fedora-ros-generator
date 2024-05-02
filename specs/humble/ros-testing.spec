# Meta Package
Name:           ros-humble-ros-testing
Version:        0.4.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ros_testing and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ros_testing
Requires:       ros2-humble-ros_testing-devel

Obsoletes: ros-humble-ros-testing < 0.4.0-1

%description
The entry point package to launch testing in ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.4.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.4.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.4.0-1
- Initial humble build
