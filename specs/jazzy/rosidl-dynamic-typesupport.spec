# Meta Package
Name:           ros-jazzy-rosidl-dynamic-typesupport
Version:        0.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_dynamic_typesupport and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_dynamic_typesupport
Requires:       ros2-jazzy-rosidl_dynamic_typesupport-devel

Obsoletes: ros-jazzy-rosidl-dynamic-typesupport < 0.1.2-1

%description
Unified serialization support interface for dynamic typesupport in C.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.1.2-1
- Update to latest release
