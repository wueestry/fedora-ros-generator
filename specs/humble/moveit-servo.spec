# Meta Package
Name:           ros-humble-moveit-servo
Version:        2.5.5
Release:        1%{?dist}
License:        BSD 3-Clause
URL:            https://ros-planning.github.io/moveit_tutorials
Summary:        Meta package for ros2-humble-moveit_servo and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-moveit_servo
Requires:       ros2-humble-moveit_servo-devel

Obsoletes: ros-humble-moveit-servo < 2.5.5-1

%description
Provides real-time manipulator Cartesian and joint servoing.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.5-1
- update to latest release
