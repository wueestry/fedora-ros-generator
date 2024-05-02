# Meta Package
Name:           ros-jazzy-action-msgs
Version:        2.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-action_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-action_msgs
Requires:       ros2-jazzy-action_msgs-devel

Obsoletes: ros-jazzy-action-msgs < 2.0.2-1

%description
Messages and service definitions common among all ROS actions.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.2-1
- Update to latest release
