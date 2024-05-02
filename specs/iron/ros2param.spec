# Meta Package
Name:           ros-iron-ros2param
Version:        0.25.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ros2param and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ros2param
Requires:       ros2-iron-ros2param-devel

Obsoletes: ros-iron-ros2param < 0.25.6-1

%description
The param command for ROS 2 command line tools.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.25.6-1
- Update to latest release
