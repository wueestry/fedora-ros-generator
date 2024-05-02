# Meta Package
Name:           ros-iron-ros-testing
Version:        0.5.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ros_testing and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ros_testing
Requires:       ros2-iron-ros_testing-devel

Obsoletes: ros-iron-ros-testing < 0.5.2-1

%description
The entry point package to launch testing in ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.5.2-1
- Update to latest release
