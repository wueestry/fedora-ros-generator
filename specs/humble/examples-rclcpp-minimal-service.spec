# Meta Package
Name:           ros-humble-examples-rclcpp-minimal-service
Version:        0.15.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-examples_rclcpp_minimal_service and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-examples_rclcpp_minimal_service
Requires:       ros2-humble-examples_rclcpp_minimal_service-devel

Obsoletes: ros-humble-examples-rclcpp-minimal-service < 0.15.2-1

%description
A minimal service server which adds two numbers

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.2-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.1-1
- Initial humble build
