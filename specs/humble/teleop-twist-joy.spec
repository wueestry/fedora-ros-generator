# Meta Package
Name:           ros-humble-teleop-twist-joy
Version:        2.4.5
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/teleop_twist_joy
Summary:        Meta package for ros2-humble-teleop_twist_joy and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-teleop_twist_joy
Requires:       ros2-humble-teleop_twist_joy-devel

Obsoletes: ros-humble-teleop-twist-joy < 2.4.5-1

%description
Generic joystick teleop for twist robots.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.5-1
- update to latest upstream release
* Thu Jun 29 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.5-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.3-1
- Initial humble build
