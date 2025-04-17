# Meta Package
Name:           ros-jazzy-webots-ros2-tesla
Version:        2025.0.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-jazzy-webots_ros2_tesla and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-webots_ros2_tesla
Requires:       ros2-jazzy-webots_ros2_tesla-devel

Obsoletes: ros-jazzy-webots-ros2-tesla < 2025.0.0-1

%description
Tesla ROS2 interface for Webots.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2025.0.0-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2023.1.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2023.1.2-1
- Update to latest release
