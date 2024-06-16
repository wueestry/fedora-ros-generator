# Meta Package
Name:           ros-humble-pendulum-msgs
Version:        0.20.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-pendulum_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-pendulum_msgs
Requires:       ros2-humble-pendulum_msgs-devel

Obsoletes: ros-humble-pendulum-msgs < 0.20.4-1

%description
Custom messages for real-time pendulum control.

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
