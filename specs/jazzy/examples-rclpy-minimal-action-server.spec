# Meta Package
Name:           ros-jazzy-examples-rclpy-minimal-action-server
Version:        0.19.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-examples_rclpy_minimal_action_server and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-examples_rclpy_minimal_action_server
Requires:       ros2-jazzy-examples_rclpy_minimal_action_server-devel

Obsoletes: ros-jazzy-examples-rclpy-minimal-action-server < 0.19.3-1

%description
Examples of minimal action servers using rclpy.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.19.3-1
- Update to latest release
