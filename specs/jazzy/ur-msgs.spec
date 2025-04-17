# Meta Package
Name:           ros-jazzy-ur-msgs
Version:        2.2.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ur_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ur_msgs
Requires:       ros2-jazzy-ur_msgs-devel

Obsoletes: ros-jazzy-ur-msgs < 2.2.0-1

%description
Message and service definitions for interacting with Universal Robots
robot controllers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.2.0-1
- Update to latest release
