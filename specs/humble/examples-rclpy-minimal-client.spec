# Meta Package
Name:           ros-humble-examples-rclpy-minimal-client
Version:        0.15.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-examples_rclpy_minimal_client and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-examples_rclpy_minimal_client
Requires:       ros2-humble-examples_rclpy_minimal_client-devel

Obsoletes: ros-humble-examples-rclpy-minimal-client < 0.15.2-1

%description
Examples of minimal service clients using rclpy.

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
