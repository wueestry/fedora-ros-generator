# Meta Package
Name:           ros-iron-rclpy
Version:        4.1.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rclpy and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rclpy
Requires:       ros2-iron-rclpy-devel

Obsoletes: ros-iron-rclpy < 4.1.5-1

%description
Package containing the Python client.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.1.5-1
- Update to latest release
