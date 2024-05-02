# Meta Package
Name:           ros-iron-rosidl-typesupport-fastrtps-cpp
Version:        3.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_typesupport_fastrtps_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_typesupport_fastrtps_cpp
Requires:       ros2-iron-rosidl_typesupport_fastrtps_cpp-devel

Obsoletes: ros-iron-rosidl-typesupport-fastrtps-cpp < 3.0.2-1

%description
Generate the C++ interfaces for eProsima FastRTPS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.0.2-1
- Update to latest release
