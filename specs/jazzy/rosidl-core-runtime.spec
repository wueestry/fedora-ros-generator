# Meta Package
Name:           ros-jazzy-rosidl-core-runtime
Version:        0.2.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_core_runtime and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_core_runtime
Requires:       ros2-jazzy-rosidl_core_runtime-devel

Obsoletes: ros-jazzy-rosidl-core-runtime < 0.2.0-1

%description
A configuration package defining runtime dependencies for core ROS
interfaces.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.2.0-1
- Update to latest release
