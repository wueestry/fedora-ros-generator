# Meta Package
Name:           ros-jazzy-kinematics-interface-kdl
Version:        1.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-kinematics_interface_kdl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-kinematics_interface_kdl
Requires:       ros2-jazzy-kinematics_interface_kdl-devel

Obsoletes: ros-jazzy-kinematics-interface-kdl < 1.1.0-1

%description
KDL implementation of ros2_control kinematics interface

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.1.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.0-1
- Update to latest release
