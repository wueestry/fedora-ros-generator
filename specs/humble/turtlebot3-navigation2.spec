# Meta Package
Name:           ros-humble-turtlebot3-navigation2
Version:        2.1.5
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://turtlebot3.robotis.com
Summary:        Meta package for ros2-humble-turtlebot3_navigation2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-turtlebot3_navigation2
Requires:       ros2-humble-turtlebot3_navigation2-devel

Obsoletes: ros-humble-turtlebot3-navigation2 < 2.1.5-1

%description
ROS 2 launch scripts for navigation2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.5-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.1.5-1
- update to latest release
