# Meta Package
Name:           ros-iron-moveit-servo
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://ros-planning.github.io/moveit_tutorials
Summary:        Meta package for ros2-iron-moveit_servo and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_servo
Requires:       ros2-iron-moveit_servo-devel

Obsoletes: ros-iron-moveit-servo < 2.8.0-1

%description
Provides real-time manipulator Cartesian and joint servoing.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
