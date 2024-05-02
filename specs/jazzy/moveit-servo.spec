# Meta Package
Name:           ros-jazzy-moveit-servo
Version:        2.9.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://ros-planning.github.io/moveit_tutorials
Summary:        Meta package for ros2-jazzy-moveit_servo and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_servo
Requires:       ros2-jazzy-moveit_servo-devel

Obsoletes: ros-jazzy-moveit-servo < 2.9.0-1

%description
Provides real-time manipulator Cartesian and joint servoing.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
