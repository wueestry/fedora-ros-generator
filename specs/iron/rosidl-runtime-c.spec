# Meta Package
Name:           ros-iron-rosidl-runtime-c
Version:        4.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_runtime_c and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_runtime_c
Requires:       ros2-iron-rosidl_runtime_c-devel

Obsoletes: ros-iron-rosidl-runtime-c < 4.0.1-1

%description
Provides definitions, initialization and finalization functions, and
macros for getting and working with rosidl typesupport types in C.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.0.1-1
- Update to latest release
