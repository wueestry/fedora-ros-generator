# Meta Package
Name:           ros-humble-teleop-twist-keyboard
Version:        2.4.0
Release:        1%{?dist}
License:        BSD License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-teleop_twist_keyboard and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-teleop_twist_keyboard
Requires:       ros2-humble-teleop_twist_keyboard-devel

Obsoletes: ros-humble-teleop-twist-keyboard < 2.4.0-1

%description
A robot-agnostic teleoperation node to convert keyboard commands to
Twist messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.0-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.2-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.2-1
- Initial humble build
