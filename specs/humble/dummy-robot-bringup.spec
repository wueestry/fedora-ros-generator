# Meta Package
Name:           ros-humble-dummy-robot-bringup
Version:        0.20.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-dummy_robot_bringup and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-dummy_robot_bringup
Requires:       ros2-humble-dummy_robot_bringup-devel

Obsoletes: ros-humble-dummy-robot-bringup < 0.20.4-1

%description
dummy robot bringup

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.4-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- Initial humble build
