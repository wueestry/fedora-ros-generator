# Meta Package
Name:           ros-jazzy-rosidl-typesupport-fastrtps-c
Version:        3.6.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_typesupport_fastrtps_c and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_typesupport_fastrtps_c
Requires:       ros2-jazzy-rosidl_typesupport_fastrtps_c-devel

Obsoletes: ros-jazzy-rosidl-typesupport-fastrtps-c < 3.6.1-1

%description
Generate the C interfaces for eProsima FastRTPS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.6.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.6.0-1
- Update to latest release
