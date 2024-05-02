# Meta Package
Name:           ros-iron-pilz-industrial-motion-planner-testutils
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-iron-pilz_industrial_motion_planner_testutils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-pilz_industrial_motion_planner_testutils
Requires:       ros2-iron-pilz_industrial_motion_planner_testutils-devel

Obsoletes: ros-iron-pilz-industrial-motion-planner-testutils < 2.8.0-1

%description
Helper scripts and functionality to test industrial motion generation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
