# Meta Package
Name:           ros-jazzy-dwb-plugins
Version:        1.3.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-dwb_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-dwb_plugins
Requires:       ros2-jazzy-dwb_plugins-devel

Obsoletes: ros-jazzy-dwb-plugins < 1.3.2-1

%description
Standard implementations of the GoalChecker and TrajectoryGenerators
for dwb_core

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
