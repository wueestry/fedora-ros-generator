# Meta Package
Name:           ros-jazzy-rosidl-dynamic-typesupport-fastrtps
Version:        0.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_dynamic_typesupport_fastrtps and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_dynamic_typesupport_fastrtps
Requires:       ros2-jazzy-rosidl_dynamic_typesupport_fastrtps-devel

Obsoletes: ros-jazzy-rosidl-dynamic-typesupport-fastrtps < 0.1.0-1

%description
FastDDS serialization support implementation for use with C/C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.1.0-1
- Update to latest release
