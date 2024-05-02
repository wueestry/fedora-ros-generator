# Meta Package
Name:           ros-humble-kinematics-interface-kdl
Version:        0.3.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-kinematics_interface_kdl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-kinematics_interface_kdl
Requires:       ros2-humble-kinematics_interface_kdl-devel

Obsoletes: ros-humble-kinematics-interface-kdl < 0.3.0-1

%description
KDL implementation of ros2_control kinematics interface

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.3.0-1
- Update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.0-1
- update to latest upstream
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.0-1
- update to latest release
