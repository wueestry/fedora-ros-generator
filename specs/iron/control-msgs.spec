# Meta Package
Name:           ros-iron-control-msgs
Version:        5.1.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-control_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-control_msgs
Requires:       ros2-iron-control_msgs-devel

Obsoletes: ros-iron-control-msgs < 5.1.0-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.5.1.0-1
- Update to latest release
