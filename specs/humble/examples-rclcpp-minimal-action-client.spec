# Meta Package
Name:           ros-humble-examples-rclcpp-minimal-action-client
Version:        0.15.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-examples_rclcpp_minimal_action_client and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-examples_rclcpp_minimal_action_client
Requires:       ros2-humble-examples_rclcpp_minimal_action_client-devel

Obsoletes: ros-humble-examples-rclcpp-minimal-action-client < 0.15.1-1

%description
Minimal action client examples

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.1-1
- Initial humble build
