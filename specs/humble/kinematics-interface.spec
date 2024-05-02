# Meta Package
Name:           ros-humble-kinematics-interface
Version:        0.3.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-kinematics_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-kinematics_interface
Requires:       ros2-humble-kinematics_interface-devel

Obsoletes: ros-humble-kinematics-interface < 0.3.0-1

%description
Kinematics interface for ROS 2 control

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
