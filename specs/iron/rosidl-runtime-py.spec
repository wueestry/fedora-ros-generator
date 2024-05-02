# Meta Package
Name:           ros-iron-rosidl-runtime-py
Version:        0.12.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_runtime_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_runtime_py
Requires:       ros2-iron-rosidl_runtime_py-devel

Obsoletes: ros-iron-rosidl-runtime-py < 0.12.0-1

%description
Runtime utilities for working with generated ROS interfaces in Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.12.0-1
- Update to latest release
