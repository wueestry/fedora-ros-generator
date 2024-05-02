# Meta Package
Name:           ros-jazzy-ros2test
Version:        0.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2test and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2test
Requires:       ros2-jazzy-ros2test-devel

Obsoletes: ros-jazzy-ros2test < 0.6.0-1

%description
The test command for ROS 2 launch tests.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.6.0-1
- Update to latest release
