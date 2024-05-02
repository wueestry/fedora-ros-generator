# Meta Package
Name:           ros-jazzy-pilz-industrial-motion-planner-testutils
Version:        2.9.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-pilz_industrial_motion_planner_testutils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pilz_industrial_motion_planner_testutils
Requires:       ros2-jazzy-pilz_industrial_motion_planner_testutils-devel

Obsoletes: ros-jazzy-pilz-industrial-motion-planner-testutils < 2.9.0-1

%description
Helper scripts and functionality to test industrial motion generation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
