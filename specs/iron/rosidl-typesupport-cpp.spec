# Meta Package
Name:           ros-iron-rosidl-typesupport-cpp
Version:        3.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_typesupport_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_typesupport_cpp
Requires:       ros2-iron-rosidl_typesupport_cpp-devel

Obsoletes: ros-iron-rosidl-typesupport-cpp < 3.0.1-1

%description
Generate the type support for C++ messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.0.1-1
- Update to latest release
