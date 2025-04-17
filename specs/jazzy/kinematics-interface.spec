# Meta Package
Name:           ros-jazzy-kinematics-interface
Version:        1.3.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-kinematics_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-kinematics_interface
Requires:       ros2-jazzy-kinematics_interface-devel

Obsoletes: ros-jazzy-kinematics-interface < 1.3.0-1

%description
Kinematics interface for ROS 2 control

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.0-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.2.1-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.1.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.0-1
- Update to latest release
