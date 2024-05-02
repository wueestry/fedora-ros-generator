# Meta Package
Name:           ros-humble-plansys2-msgs
Version:        2.0.9
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-plansys2_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-plansys2_msgs
Requires:       ros2-humble-plansys2_msgs-devel

Obsoletes: ros-humble-plansys2-msgs < 2.0.9-1

%description
Messages and service files for the ROS2 Planning System

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Nov 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.9-1
- update to latest release
* Thu Apr 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.9-1
- update to latest release
