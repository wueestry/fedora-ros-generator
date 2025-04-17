# Meta Package
Name:           ros-jazzy-plansys2-popf-plan-solver
Version:        2.0.18
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-plansys2_popf_plan_solver and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-plansys2_popf_plan_solver
Requires:       ros2-jazzy-plansys2_popf_plan_solver-devel

Obsoletes: ros-jazzy-plansys2-popf-plan-solver < 2.0.18-1

%description
This package contains the PDDL-based Planner module for the ROS2
Planning System

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.18-1
- Update to latest release
