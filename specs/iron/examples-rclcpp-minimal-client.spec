# Meta Package
Name:           ros-iron-examples-rclcpp-minimal-client
Version:        0.18.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-examples_rclcpp_minimal_client and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-examples_rclcpp_minimal_client
Requires:       ros2-iron-examples_rclcpp_minimal_client-devel

Obsoletes: ros-iron-examples-rclcpp-minimal-client < 0.18.0-1

%description
Examples of minimal service clients

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.18.0-1
- Update to latest release
