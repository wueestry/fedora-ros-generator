# Meta Package
Name:           ros-jazzy-rclcpp
Version:        28.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rclcpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rclcpp
Requires:       ros2-jazzy-rclcpp-devel

Obsoletes: ros-jazzy-rclcpp < 28.1.2-1

%description
The ROS client library in C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.28.1.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.28.1.1-1
- Update to latest release
