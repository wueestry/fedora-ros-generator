# Meta Package
Name:           ros-iron-ros2test
Version:        0.5.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ros2test and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ros2test
Requires:       ros2-iron-ros2test-devel

Obsoletes: ros-iron-ros2test < 0.5.2-1

%description
The test command for ROS 2 launch tests.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.5.2-1
- Update to latest release
