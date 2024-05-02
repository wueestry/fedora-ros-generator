# Meta Package
Name:           ros-jazzy-ros-base
Version:        0.10.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros_base and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros_base
Requires:       ros2-jazzy-ros_base-devel

Obsoletes: ros-jazzy-ros-base < 0.10.0-1

%description
A package which extends 'ros_core' and includes other basic
functionalities like tf2 and urdf.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.10.0-1
- Update to latest release
