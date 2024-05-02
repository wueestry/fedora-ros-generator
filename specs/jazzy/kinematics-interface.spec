# Meta Package
Name:           ros-jazzy-kinematics-interface
Version:        1.0.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-kinematics_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-kinematics_interface
Requires:       ros2-jazzy-kinematics_interface-devel

Obsoletes: ros-jazzy-kinematics-interface < 1.0.0-1

%description
Kinematics interface for ROS 2 control

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.0-1
- Update to latest release
