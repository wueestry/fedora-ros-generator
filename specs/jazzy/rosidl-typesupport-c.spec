# Meta Package
Name:           ros-jazzy-rosidl-typesupport-c
Version:        3.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_typesupport_c and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_typesupport_c
Requires:       ros2-jazzy-rosidl_typesupport_c-devel

Obsoletes: ros-jazzy-rosidl-typesupport-c < 3.2.2-1

%description
Generate the type support for C messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.2.2-1
- Update to latest release
