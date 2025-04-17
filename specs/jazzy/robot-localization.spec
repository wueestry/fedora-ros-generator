# Meta Package
Name:           ros-jazzy-robot-localization
Version:        3.8.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://ros.org/wiki/robot_localization
Summary:        Meta package for ros2-jazzy-robot_localization and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-robot_localization
Requires:       ros2-jazzy-robot_localization-devel

Obsoletes: ros-jazzy-robot-localization < 3.8.2-1

%description
Provides nonlinear state estimation through sensor fusion of an
abritrary number of sensors.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.8.2-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.8.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.8.0-1
- Update to latest release
