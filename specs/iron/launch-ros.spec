# Meta Package
Name:           ros-iron-launch-ros
Version:        0.24.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-launch_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-launch_ros
Requires:       ros2-iron-launch_ros-devel

Obsoletes: ros-iron-launch-ros < 0.24.1-1

%description
ROS specific extensions to the launch tool.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.24.1-1
- Update to latest release
