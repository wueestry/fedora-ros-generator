# Meta Package
Name:           ros-iron-rclcpp-components
Version:        21.0.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rclcpp_components and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rclcpp_components
Requires:       ros2-iron-rclcpp_components-devel

Obsoletes: ros-iron-rclcpp-components < 21.0.6-1

%description
Package containing tools for dynamically loadable components

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.21.0.6-1
- Update to latest release
