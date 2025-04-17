# Meta Package
Name:           ros-jazzy-examples-rclcpp-minimal-action-client
Version:        0.19.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-examples_rclcpp_minimal_action_client and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-examples_rclcpp_minimal_action_client
Requires:       ros2-jazzy-examples_rclcpp_minimal_action_client-devel

Obsoletes: ros-jazzy-examples-rclcpp-minimal-action-client < 0.19.5-1

%description
Minimal action client examples

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.19.5-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.19.4-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.19.3-1
- Update to latest release
