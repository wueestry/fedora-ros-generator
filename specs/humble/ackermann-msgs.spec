# Meta Package
Name:           ros-humble-ackermann-msgs
Version:        2.0.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ackermann_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ackermann_msgs
Requires:       ros2-humble-ackermann_msgs-devel

Obsoletes: ros-humble-ackermann-msgs < 2.0.2-1

%description
ROS2 messages for robots using Ackermann steering.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.2-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.2-1
- update to latest release
