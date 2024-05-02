# Meta Package
Name:           ros-iron-kinematics-interface-kdl
Version:        1.0.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-kinematics_interface_kdl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-kinematics_interface_kdl
Requires:       ros2-iron-kinematics_interface_kdl-devel

Obsoletes: ros-iron-kinematics-interface-kdl < 1.0.0-1

%description
KDL implementation of ros2_control kinematics interface

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.0-1
- Update to latest release
