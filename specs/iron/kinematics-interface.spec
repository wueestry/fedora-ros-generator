# Meta Package
Name:           ros-iron-kinematics-interface
Version:        1.0.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-kinematics_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-kinematics_interface
Requires:       ros2-iron-kinematics_interface-devel

Obsoletes: ros-iron-kinematics-interface < 1.0.0-1

%description
Kinematics interface for ROS 2 control

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.0-1
- Update to latest release
