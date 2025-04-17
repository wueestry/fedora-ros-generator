# Meta Package
Name:           ros-jazzy-ros-gz-bridge
Version:        1.0.11
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros_gz_bridge and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros_gz_bridge
Requires:       ros2-jazzy-ros_gz_bridge-devel

Obsoletes: ros-jazzy-ros-gz-bridge < 1.0.11-1

%description
Bridge communication between ROS and Gazebo Transport

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.11-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.9-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.7-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.5-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.3-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.2-1
- Update to latest release
