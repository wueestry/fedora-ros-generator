# Meta Package
Name:           ros-jazzy-actuator-msgs
Version:        0.0.1
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-actuator_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-actuator_msgs
Requires:       ros2-jazzy-actuator_msgs-devel

Obsoletes: ros-jazzy-actuator-msgs < 0.0.1-1

%description
ROS 2 message interface for Actuators.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.1-1
- Update to latest release
