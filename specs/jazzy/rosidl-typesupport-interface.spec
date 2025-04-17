# Meta Package
Name:           ros-jazzy-rosidl-typesupport-interface
Version:        4.6.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_typesupport_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_typesupport_interface
Requires:       ros2-jazzy-rosidl_typesupport_interface-devel

Obsoletes: ros-jazzy-rosidl-typesupport-interface < 4.6.5-1

%description
The interface for rosidl typesupport packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.5-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.4-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.3-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.1-1
- Update to latest release
