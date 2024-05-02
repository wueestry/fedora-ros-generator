# Meta Package
Name:           ros-jazzy-ackermann-msgs
Version:        2.0.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ackermann_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ackermann_msgs
Requires:       ros2-jazzy-ackermann_msgs-devel

Obsoletes: ros-jazzy-ackermann-msgs < 2.0.2-1

%description
ROS2 messages for robots using Ackermann steering.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.2-1
- Update to latest release
