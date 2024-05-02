# Meta Package
Name:           ros-iron-tf2-ros
Version:        0.31.6
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/tf2_ros
Summary:        Meta package for ros2-iron-tf2_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tf2_ros
Requires:       ros2-iron-tf2_ros-devel

Obsoletes: ros-iron-tf2-ros < 0.31.6-1

%description
This package contains the C++ ROS bindings for the tf2 library

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.6-1
- Update to latest release
