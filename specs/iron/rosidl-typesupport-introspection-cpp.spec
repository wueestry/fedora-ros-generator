# Meta Package
Name:           ros-iron-rosidl-typesupport-introspection-cpp
Version:        4.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_typesupport_introspection_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_typesupport_introspection_cpp
Requires:       ros2-iron-rosidl_typesupport_introspection_cpp-devel

Obsoletes: ros-iron-rosidl-typesupport-introspection-cpp < 4.0.1-1

%description
Generate the message type support for dynamic message construction in
C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.0.1-1
- Update to latest release
