# Meta Package
Name:           ros-iron-robot-localization
Version:        3.7.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://ros.org/wiki/robot_localization
Summary:        Meta package for ros2-iron-robot_localization and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-robot_localization
Requires:       ros2-iron-robot_localization-devel

Obsoletes: ros-iron-robot-localization < 3.7.0-1

%description
Provides nonlinear state estimation through sensor fusion of an
abritrary number of sensors.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.7.0-1
- Update to latest release
