# Meta Package
Name:           ros-jazzy-rosidl-runtime-cpp
Version:        4.6.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_runtime_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_runtime_cpp
Requires:       ros2-jazzy-rosidl_runtime_cpp-devel

Obsoletes: ros-jazzy-rosidl-runtime-cpp < 4.6.2-1

%description
Provides definitions and templated functions for getting and working
with rosidl typesupport types in C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.1-1
- Update to latest release
