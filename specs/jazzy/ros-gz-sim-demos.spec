# Meta Package
Name:           ros-jazzy-ros-gz-sim-demos
Version:        1.0.11
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros_gz_sim_demos and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros_gz_sim_demos
Requires:       ros2-jazzy-ros_gz_sim_demos-devel

Obsoletes: ros-jazzy-ros-gz-sim-demos < 1.0.11-1

%description
Demos using Gazebo Sim simulation with ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 17 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.11-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.7-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.5-1
- Update to latest release
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.3-1
- Update to latest release
