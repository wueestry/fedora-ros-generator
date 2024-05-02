# Meta Package
Name:           ros-humble-robot-localization
Version:        3.5.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://ros.org/wiki/robot_localization
Summary:        Meta package for ros2-humble-robot_localization and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-robot_localization
Requires:       ros2-humble-robot_localization-devel

Obsoletes: ros-humble-robot-localization < 3.5.3-1

%description
Provides nonlinear state estimation through sensor fusion of an
abritrary number of sensors.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 25 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.5.3-1
- Update to latest release
* Mon Feb 12 2024 Tarik Viehmann - humble.3.5.2-1
- update to latest release
