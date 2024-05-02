# Meta Package
Name:           ros-iron-examples-rclpy-executors
Version:        0.18.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-examples_rclpy_executors and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-examples_rclpy_executors
Requires:       ros2-iron-examples_rclpy_executors-devel

Obsoletes: ros-iron-examples-rclpy-executors < 0.18.0-1

%description
Examples of creating and using exectors to run multiple nodes in the
same process

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.18.0-1
- Update to latest release
