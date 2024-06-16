# Meta Package
Name:           ros-iron-ros2-control
Version:        3.25.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ros2_control and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ros2_control
Requires:       ros2-iron-ros2_control-devel

Obsoletes: ros-iron-ros2-control < 3.25.0-1

%description
Metapackage for ROS2 control related packages

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.25.0-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
