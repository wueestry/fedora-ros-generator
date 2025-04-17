# Meta Package
Name:           ros-jazzy-parallel-gripper-controller
Version:        4.23.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://control.ros.org
Summary:        Meta package for ros2-jazzy-parallel_gripper_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-parallel_gripper_controller
Requires:       ros2-jazzy-parallel_gripper_controller-devel

Obsoletes: ros-jazzy-parallel-gripper-controller < 4.23.0-1

%description
The parallel_gripper_controller package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sun Apr 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.23.0-1
- Update to latest release
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.22.0-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.21.0-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.18.0-1
- Update to latest release
