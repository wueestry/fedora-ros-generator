# Meta Package
Name:           ros-jazzy-joint-limits
Version:        4.8.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/ros-controls/ros2_control/wiki
Summary:        Meta package for ros2-jazzy-joint_limits and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-joint_limits
Requires:       ros2-jazzy-joint_limits-devel

Obsoletes: ros-jazzy-joint-limits < 4.8.0-1

%description
Interfaces for handling of joint limits for controllers or hardware.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.8.0-1
- Update to latest release
