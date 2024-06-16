# Meta Package
Name:           ros-iron-joint-limits
Version:        3.25.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ros-controls/ros2_control/wiki
Summary:        Meta package for ros2-iron-joint_limits and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-joint_limits
Requires:       ros2-iron-joint_limits-devel

Obsoletes: ros-iron-joint-limits < 3.25.0-1

%description
Interfaces for handling of joint limits for controllers or hardware.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.25.0-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
