# Meta Package
Name:           ros-jazzy-actionlib-msgs
Version:        5.3.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-actionlib_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-actionlib_msgs
Requires:       ros2-jazzy-actionlib_msgs-devel

Obsoletes: ros-jazzy-actionlib-msgs < 5.3.5-1

%description
A package containing some message definitions used in the
implementation of ROS 1 actions.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.5-1
- Update to latest release
