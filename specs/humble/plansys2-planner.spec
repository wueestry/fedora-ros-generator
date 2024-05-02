# Meta Package
Name:           ros-humble-plansys2-planner
Version:        2.0.9
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-plansys2_planner and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-plansys2_planner
Requires:       ros2-humble-plansys2_planner-devel

Obsoletes: ros-humble-plansys2-planner < 2.0.9-1

%description
This package contains the PDDL-based Planner module for the ROS2
Planning System

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
