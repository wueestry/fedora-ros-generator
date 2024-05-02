# Meta Package
Name:           ros-jazzy-joint-trajectory-controller
Version:        4.7.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-joint_trajectory_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-joint_trajectory_controller
Requires:       ros2-jazzy-joint_trajectory_controller-devel

Obsoletes: ros-jazzy-joint-trajectory-controller < 4.7.0-1

%description
Controller for executing joint-space trajectories on a group of joints

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.7.0-1
- Update to latest release
