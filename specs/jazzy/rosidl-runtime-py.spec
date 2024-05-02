# Meta Package
Name:           ros-jazzy-rosidl-runtime-py
Version:        0.13.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_runtime_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_runtime_py
Requires:       ros2-jazzy-rosidl_runtime_py-devel

Obsoletes: ros-jazzy-rosidl-runtime-py < 0.13.1-1

%description
Runtime utilities for working with generated ROS interfaces in Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.13.1-1
- Update to latest release
