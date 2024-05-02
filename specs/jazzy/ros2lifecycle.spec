# Meta Package
Name:           ros-jazzy-ros2lifecycle
Version:        0.32.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2lifecycle and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2lifecycle
Requires:       ros2-jazzy-ros2lifecycle-devel

Obsoletes: ros-jazzy-ros2lifecycle < 0.32.0-1

%description
The lifecycle command for ROS 2 command line tools.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.32.0-1
- Update to latest release
