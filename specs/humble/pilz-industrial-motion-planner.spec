# Meta Package
Name:           ros-humble-pilz-industrial-motion-planner
Version:        2.5.5
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-humble-pilz_industrial_motion_planner and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-pilz_industrial_motion_planner
Requires:       ros2-humble-pilz_industrial_motion_planner-devel

Obsoletes: ros-humble-pilz-industrial-motion-planner < 2.5.5-1

%description
MoveIt plugin to generate industrial trajectories PTP, LIN, CIRC and
sequences thereof.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.5-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.4-1
- Initial humble build
