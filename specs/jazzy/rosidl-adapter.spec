# Meta Package
Name:           ros-jazzy-rosidl-adapter
Version:        4.6.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_adapter and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_adapter
Requires:       ros2-jazzy-rosidl_adapter-devel

Obsoletes: ros-jazzy-rosidl-adapter < 4.6.2-1

%description
API and scripts to parse .msg/.srv/.action files and convert them to
.idl.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.1-1
- Update to latest release
