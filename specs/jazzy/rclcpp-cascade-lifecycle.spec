# Meta Package
Name:           ros-jazzy-rclcpp-cascade-lifecycle
Version:        2.0.0
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rclcpp_cascade_lifecycle and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rclcpp_cascade_lifecycle
Requires:       ros2-jazzy-rclcpp_cascade_lifecycle-devel

Obsoletes: ros-jazzy-rclcpp-cascade-lifecycle < 2.0.0-1

%description
Provides a mechanism to make trees of lifecycle nodes to propagate
state changes

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.0-1
- Update to latest release
