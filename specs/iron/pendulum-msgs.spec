# Meta Package
Name:           ros-iron-pendulum-msgs
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-pendulum_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-pendulum_msgs
Requires:       ros2-iron-pendulum_msgs-devel

Obsoletes: ros-iron-pendulum-msgs < 0.27.1-1

%description
Custom messages for real-time pendulum control.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
