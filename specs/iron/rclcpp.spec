# Meta Package
Name:           ros-iron-rclcpp
Version:        21.0.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rclcpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rclcpp
Requires:       ros2-iron-rclcpp-devel

Obsoletes: ros-iron-rclcpp < 21.0.6-1

%description
The ROS client library in C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.21.0.6-1
- Update to latest release
