# Meta Package
Name:           ros-jazzy-control-msgs
Version:        5.4.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://control.ros.org
Summary:        Meta package for ros2-jazzy-control_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-control_msgs
Requires:       ros2-jazzy-control_msgs-devel

Obsoletes: ros-jazzy-control-msgs < 5.4.0-1

%description
control_msgs contains base messages and actions useful for controlling
robots. It provides representations for controller setpoints and joint
and cartesian trajectories.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.4.0-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.0-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.2.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.0-1
- Update to latest release
