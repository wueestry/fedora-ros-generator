# Meta Package
Name:           ros-jazzy-chomp-motion-planner
Version:        2.12.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-chomp_motion_planner and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-chomp_motion_planner
Requires:       ros2-jazzy-chomp_motion_planner-devel

Obsoletes: ros-jazzy-chomp-motion-planner < 2.12.2-1

%description
chomp_motion_planner

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
