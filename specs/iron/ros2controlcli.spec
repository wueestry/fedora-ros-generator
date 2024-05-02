# Meta Package
Name:           ros-iron-ros2controlcli
Version:        3.24.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ros2controlcli and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ros2controlcli
Requires:       ros2-iron-ros2controlcli-devel

Obsoletes: ros-iron-ros2controlcli < 3.24.0-1

%description
The ROS 2 command line tools for ROS2 Control.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
