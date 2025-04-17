# Meta Package
Name:           ros-jazzy-webots-ros2-husarion
Version:        2025.0.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-jazzy-webots_ros2_husarion and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-webots_ros2_husarion
Requires:       ros2-jazzy-webots_ros2_husarion-devel

Obsoletes: ros-jazzy-webots-ros2-husarion < 2025.0.0-1

%description
Husarion ROSbot 2R and XL robots ROS2 interface for Webots.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2025.0.0-1
- Update to latest release
