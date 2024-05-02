# Meta Package
Name:           ros-jazzy-joy
Version:        3.3.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-joy and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-joy
Requires:       ros2-jazzy-joy-devel

Obsoletes: ros-jazzy-joy < 3.3.0-1

%description
The joy package contains joy_node, a node that interfaces a generic
joystick to ROS 2. This node publishes a "Joy" message, which contains
the current state of each one of the joystick's buttons and axes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.3.0-1
- Update to latest release
