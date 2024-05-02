# Meta Package
Name:           ros-iron-ackermann-msgs
Version:        2.0.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ackermann_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ackermann_msgs
Requires:       ros2-iron-ackermann_msgs-devel

Obsoletes: ros-iron-ackermann-msgs < 2.0.2-1

%description
ROS2 messages for robots using Ackermann steering.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.2-1
- Update to latest release
