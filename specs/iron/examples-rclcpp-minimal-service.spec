# Meta Package
Name:           ros-iron-examples-rclcpp-minimal-service
Version:        0.18.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-examples_rclcpp_minimal_service and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-examples_rclcpp_minimal_service
Requires:       ros2-iron-examples_rclcpp_minimal_service-devel

Obsoletes: ros-iron-examples-rclcpp-minimal-service < 0.18.0-1

%description
A minimal service server which adds two numbers

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.18.0-1
- Update to latest release
