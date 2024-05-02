# Meta Package
Name:           ros-humble-joint-limits
Version:        2.40.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ros-controls/ros2_control/wiki
Summary:        Meta package for ros2-humble-joint_limits and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-joint_limits
Requires:       ros2-humble-joint_limits-devel

Obsoletes: ros-humble-joint-limits < 2.40.0-1

%description
Interfaces for handling of joint limits for controllers or hardware.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.40.0-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.39.1-1
- Update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.35.1-1
- update to latest upstream
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.33.0-1
- update to latest release
* Mon Apr 17 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.25.1-1
- update to latest release
