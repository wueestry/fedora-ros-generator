# Meta Package
Name:           ros-jazzy-rosidl-cmake
Version:        4.6.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_cmake and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_cmake
Requires:       ros2-jazzy-rosidl_cmake-devel

Obsoletes: ros-jazzy-rosidl-cmake < 4.6.1-1

%description
The CMake functionality to invoke code generation for ROS interface
files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.1-1
- Update to latest release
