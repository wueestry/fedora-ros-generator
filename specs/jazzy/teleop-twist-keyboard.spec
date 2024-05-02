# Meta Package
Name:           ros-jazzy-teleop-twist-keyboard
Version:        2.4.0
Release:        1%{?dist}
License:        BSD License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-teleop_twist_keyboard and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-teleop_twist_keyboard
Requires:       ros2-jazzy-teleop_twist_keyboard-devel

Obsoletes: ros-jazzy-teleop-twist-keyboard < 2.4.0-1

%description
A robot-agnostic teleoperation node to convert keyboard commands to
Twist messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.4.0-1
- Update to latest release
