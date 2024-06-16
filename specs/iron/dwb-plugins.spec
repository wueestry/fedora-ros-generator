# Meta Package
Name:           ros-iron-dwb-plugins
Version:        1.2.9
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-dwb_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-dwb_plugins
Requires:       ros2-iron-dwb_plugins-devel

Obsoletes: ros-iron-dwb-plugins < 1.2.9-1

%description
Standard implementations of the GoalChecker and TrajectoryGenerators
for dwb_core

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.9-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.8-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
