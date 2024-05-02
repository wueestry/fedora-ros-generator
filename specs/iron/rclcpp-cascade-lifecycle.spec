# Meta Package
Name:           ros-iron-rclcpp-cascade-lifecycle
Version:        1.0.5
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rclcpp_cascade_lifecycle and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rclcpp_cascade_lifecycle
Requires:       ros2-iron-rclcpp_cascade_lifecycle-devel

Obsoletes: ros-iron-rclcpp-cascade-lifecycle < 1.0.5-1

%description
Provides a mechanism to make trees of lifecycle nodes to propagate
state changes

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.5-1
- Update to latest release
