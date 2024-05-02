# Meta Package
Name:           ros-iron-webots-ros2-tests
Version:        2023.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-iron-webots_ros2_tests and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-webots_ros2_tests
Requires:       ros2-iron-webots_ros2_tests-devel

Obsoletes: ros-iron-webots-ros2-tests < 2023.1.2-1

%description
System tests for `webots_ros2` packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2023.1.2-1
- Update to latest release
