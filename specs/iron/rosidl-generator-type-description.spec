# Meta Package
Name:           ros-iron-rosidl-generator-type-description
Version:        4.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_generator_type_description and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_generator_type_description
Requires:       ros2-iron-rosidl_generator_type_description-devel

Obsoletes: ros-iron-rosidl-generator-type-description < 4.0.1-1

%description
Generate hashes and descriptions of ROS 2 interface types, per
REP-2011.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.0.1-1
- Update to latest release
