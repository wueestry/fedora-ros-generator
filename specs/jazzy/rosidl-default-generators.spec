# Meta Package
Name:           ros-jazzy-rosidl-default-generators
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_default_generators and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_default_generators
Requires:       ros2-jazzy-rosidl_default_generators-devel

Obsoletes: ros-jazzy-rosidl-default-generators < 1.6.0-1

%description
A configuration package defining the default ROS interface generators.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.6.0-1
- Update to latest release
