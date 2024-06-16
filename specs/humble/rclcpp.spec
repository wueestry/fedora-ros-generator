# Meta Package
Name:           ros-humble-rclcpp
Version:        16.0.9
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rclcpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rclcpp
Requires:       ros2-humble-rclcpp-devel

Obsoletes: ros-humble-rclcpp < 16.0.9-1

%description
The ROS client library in C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.16.0.9-1
- Update to latest release
* Mon Feb 12 2024 Tarik Viehmann - humble.16.0.8-1
- update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.16.0.7-1
- update to latest upstream
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.16.0.6-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.16.0.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.16.0.5-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.16.0.5-1
- update to latest release
* Mon Jun 19 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.16.0.4-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.16.0.3-1
- Initial humble build
