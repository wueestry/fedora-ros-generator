# Meta Package
Name:           ros-iron-ros2-controllers
Version:        3.22.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ros2_controllers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ros2_controllers
Requires:       ros2-iron-ros2_controllers-devel

Obsoletes: ros-iron-ros2-controllers < 3.22.0-1

%description
Metapackage for ROS2 controllers related packages

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.22.0-1
- Update to latest release
