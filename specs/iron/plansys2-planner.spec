# Meta Package
Name:           ros-iron-plansys2-planner
Version:        2.0.11
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-plansys2_planner and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-plansys2_planner
Requires:       ros2-iron-plansys2_planner-devel

Obsoletes: ros-iron-plansys2-planner < 2.0.11-1

%description
This package contains the PDDL-based Planner module for the ROS2
Planning System

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.11-1
- Update to latest release
