# Meta Package
Name:           ros-iron-examples-rclpy-minimal-action-server
Version:        0.18.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-examples_rclpy_minimal_action_server and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-examples_rclpy_minimal_action_server
Requires:       ros2-iron-examples_rclpy_minimal_action_server-devel

Obsoletes: ros-iron-examples-rclpy-minimal-action-server < 0.18.0-1

%description
Examples of minimal action servers using rclpy.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.18.0-1
- Update to latest release
