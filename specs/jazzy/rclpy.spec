# Meta Package
Name:           ros-jazzy-rclpy
Version:        7.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rclpy and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rclpy
Requires:       ros2-jazzy-rclpy-devel

Obsoletes: ros-jazzy-rclpy < 7.1.1-1

%description
Package containing the Python client.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.7.1.1-1
- Update to latest release
