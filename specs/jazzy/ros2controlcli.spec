# Meta Package
Name:           ros-jazzy-ros2controlcli
Version:        4.8.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2controlcli and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2controlcli
Requires:       ros2-jazzy-ros2controlcli-devel

Obsoletes: ros-jazzy-ros2controlcli < 4.8.0-1

%description
The ROS 2 command line tools for ROS2 Control.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.8.0-1
- Update to latest release
