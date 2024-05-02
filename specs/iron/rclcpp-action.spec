# Meta Package
Name:           ros-iron-rclcpp-action
Version:        21.0.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rclcpp_action and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rclcpp_action
Requires:       ros2-iron-rclcpp_action-devel

Obsoletes: ros-iron-rclcpp-action < 21.0.6-1

%description
Adds action APIs for C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.21.0.6-1
- Update to latest release
