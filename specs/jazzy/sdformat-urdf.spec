# Meta Package
Name:           ros-jazzy-sdformat-urdf
Version:        1.0.2
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-sdformat_urdf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-sdformat_urdf
Requires:       ros2-jazzy-sdformat_urdf-devel

Obsoletes: ros-jazzy-sdformat-urdf < 1.0.2-1

%description
URDF plugin to parse SDFormat XML into URDF C++ DOM objects.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.2-1
- Update to latest release
