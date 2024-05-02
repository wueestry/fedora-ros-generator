# Meta Package
Name:           ros-jazzy-urdf-parser-plugin
Version:        2.10.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-urdf_parser_plugin and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-urdf_parser_plugin
Requires:       ros2-jazzy-urdf_parser_plugin-devel

Obsoletes: ros-jazzy-urdf-parser-plugin < 2.10.0-1

%description
This package contains a C++ base class for URDF parsers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-1
- Update to latest release
