# Meta Package
Name:           ros-iron-rosidl-dynamic-typesupport-fastrtps
Version:        0.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_dynamic_typesupport_fastrtps and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_dynamic_typesupport_fastrtps
Requires:       ros2-iron-rosidl_dynamic_typesupport_fastrtps-devel

Obsoletes: ros-iron-rosidl-dynamic-typesupport-fastrtps < 0.0.2-1

%description
FastDDS serialization support implementation for use with C/C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.0.2-1
- Update to latest release
