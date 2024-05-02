# Meta Package
Name:           ros-jazzy-rclcpp-components
Version:        28.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rclcpp_components and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rclcpp_components
Requires:       ros2-jazzy-rclcpp_components-devel

Obsoletes: ros-jazzy-rclcpp-components < 28.1.1-1

%description
Package containing tools for dynamically loadable components

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.28.1.1-1
- Update to latest release
