# Meta Package
Name:           ros-humble-pilz-industrial-motion-planner-testutils
Version:        2.5.5
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-humble-pilz_industrial_motion_planner_testutils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-pilz_industrial_motion_planner_testutils
Requires:       ros2-humble-pilz_industrial_motion_planner_testutils-devel

Obsoletes: ros-humble-pilz-industrial-motion-planner-testutils < 2.5.5-1

%description
Helper scripts and functionality to test industrial motion generation

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
