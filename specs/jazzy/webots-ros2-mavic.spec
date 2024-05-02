# Meta Package
Name:           ros-jazzy-webots-ros2-mavic
Version:        2023.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-jazzy-webots_ros2_mavic and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-webots_ros2_mavic
Requires:       ros2-jazzy-webots_ros2_mavic-devel

Obsoletes: ros-jazzy-webots-ros2-mavic < 2023.1.2-1

%description
Mavic 2 Pro robot ROS2 interface for Webots.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2023.1.2-1
- Update to latest release
