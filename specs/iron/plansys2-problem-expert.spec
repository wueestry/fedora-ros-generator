# Meta Package
Name:           ros-iron-plansys2-problem-expert
Version:        2.0.11
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-plansys2_problem_expert and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-plansys2_problem_expert
Requires:       ros2-iron-plansys2_problem_expert-devel

Obsoletes: ros-iron-plansys2-problem-expert < 2.0.11-1

%description
This package contains the Problem Expert module for the ROS2 Planning
System

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.11-1
- Update to latest release
