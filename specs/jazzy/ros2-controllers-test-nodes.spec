# Meta Package
Name:           ros-jazzy-ros2-controllers-test-nodes
Version:        4.23.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://control.ros.org
Summary:        Meta package for ros2-jazzy-ros2_controllers_test_nodes and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2_controllers_test_nodes
Requires:       ros2-jazzy-ros2_controllers_test_nodes-devel

Obsoletes: ros-jazzy-ros2-controllers-test-nodes < 4.23.0-1

%description
Demo nodes for showing and testing functionalities of the ros2_control
framework.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.23.0-1
- Update to latest release
