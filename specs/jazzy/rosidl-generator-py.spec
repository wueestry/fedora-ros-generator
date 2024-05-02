# Meta Package
Name:           ros-jazzy-rosidl-generator-py
Version:        0.22.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_generator_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_generator_py
Requires:       ros2-jazzy-rosidl_generator_py-devel

Obsoletes: ros-jazzy-rosidl-generator-py < 0.22.0-1

%description
Generate the ROS interfaces in Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.22.0-1
- Update to latest release
