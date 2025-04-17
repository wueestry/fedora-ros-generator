# Meta Package
Name:           ros-jazzy-teleop-twist-joy
Version:        2.6.3
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/teleop_twist_joy
Summary:        Meta package for ros2-jazzy-teleop_twist_joy and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-teleop_twist_joy
Requires:       ros2-jazzy-teleop_twist_joy-devel

Obsoletes: ros-jazzy-teleop-twist-joy < 2.6.3-1

%description
Generic joystick teleop for twist robots.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.6.3-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.6.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.6.0-1
- Update to latest release
