# Meta Package
Name:           ros-jazzy-webots-ros2-crazyflie
Version:        2025.0.0
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-webots_ros2_crazyflie and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-webots_ros2_crazyflie
Requires:       ros2-jazzy-webots_ros2_crazyflie-devel

Obsoletes: ros-jazzy-webots-ros2-crazyflie < 2025.0.0-1

%description
ROS2 package for Crazyflie webots simulator

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2025.0.0-1
- Update to latest release
