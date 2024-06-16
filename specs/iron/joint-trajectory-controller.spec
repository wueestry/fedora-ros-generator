# Meta Package
Name:           ros-iron-joint-trajectory-controller
Version:        3.24.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-joint_trajectory_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-joint_trajectory_controller
Requires:       ros2-iron-joint_trajectory_controller-devel

Obsoletes: ros-iron-joint-trajectory-controller < 3.24.0-1

%description
Controller for executing joint-space trajectories on a group of joints

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.22.0-1
- Update to latest release
