# Meta Package
Name:           ros-iron-rosidl-typesupport-interface
Version:        4.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_typesupport_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_typesupport_interface
Requires:       ros2-iron-rosidl_typesupport_interface-devel

Obsoletes: ros-iron-rosidl-typesupport-interface < 4.0.1-1

%description
The interface for rosidl typesupport packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.0.1-1
- Update to latest release
