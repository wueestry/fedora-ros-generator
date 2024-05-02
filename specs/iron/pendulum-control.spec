# Meta Package
Name:           ros-iron-pendulum-control
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-pendulum_control and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-pendulum_control
Requires:       ros2-iron-pendulum_control-devel

Obsoletes: ros-iron-pendulum-control < 0.27.1-1

%description
Demonstrates ROS 2's realtime capabilities with a simulated inverted
pendulum.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
