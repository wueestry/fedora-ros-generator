# Meta Package
Name:           ros-iron-rosidl-generator-c
Version:        4.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_generator_c and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_generator_c
Requires:       ros2-iron-rosidl_generator_c-devel

Obsoletes: ros-iron-rosidl-generator-c < 4.0.1-1

%description
Generate the ROS interfaces in C.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.0.1-1
- Update to latest release
