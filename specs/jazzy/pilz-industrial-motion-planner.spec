# Meta Package
Name:           ros-jazzy-pilz-industrial-motion-planner
Version:        2.12.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-pilz_industrial_motion_planner and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pilz_industrial_motion_planner
Requires:       ros2-jazzy-pilz_industrial_motion_planner-devel

Obsoletes: ros-jazzy-pilz-industrial-motion-planner < 2.12.2-1

%description
MoveIt plugin to generate industrial trajectories PTP, LIN, CIRC and
sequences thereof.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.12.2-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.12.1-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
