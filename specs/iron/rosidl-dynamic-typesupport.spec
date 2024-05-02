# Meta Package
Name:           ros-iron-rosidl-dynamic-typesupport
Version:        0.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_dynamic_typesupport and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_dynamic_typesupport
Requires:       ros2-iron-rosidl_dynamic_typesupport-devel

Obsoletes: ros-iron-rosidl-dynamic-typesupport < 0.0.5-1

%description
Unified serialization support interface for dynamic typesupport in C.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.0.5-1
- Update to latest release
