# Meta Package
Name:           ros-humble-rclcpp-cascade-lifecycle
Version:        1.1.0
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rclcpp_cascade_lifecycle and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rclcpp_cascade_lifecycle
Requires:       ros2-humble-rclcpp_cascade_lifecycle-devel

Obsoletes: ros-humble-rclcpp-cascade-lifecycle < 1.1.0-1

%description
Provides a mechanism to make trees of lifecycle nodes to propagate
state changes

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.0-1
- Update to latest release
* Thu Nov 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest release
* Thu Apr 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest release
