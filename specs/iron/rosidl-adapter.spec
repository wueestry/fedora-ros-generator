# Meta Package
Name:           ros-iron-rosidl-adapter
Version:        4.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosidl_adapter and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosidl_adapter
Requires:       ros2-iron-rosidl_adapter-devel

Obsoletes: ros-iron-rosidl-adapter < 4.0.1-1

%description
API and scripts to parse .msg/.srv/.action files and convert them to
.idl.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.0.1-1
- Update to latest release
