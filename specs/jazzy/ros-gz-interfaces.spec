# Meta Package
Name:           ros-jazzy-ros-gz-interfaces
Version:        1.0.3
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros_gz_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros_gz_interfaces
Requires:       ros2-jazzy-ros_gz_interfaces-devel

Obsoletes: ros-jazzy-ros-gz-interfaces < 1.0.3-1

%description
Message and service data structures for interacting with Gazebo from
ROS2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.3-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.2-1
- Update to latest release
