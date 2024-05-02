# Meta Package
Name:           ros-iron-urdf-parser-plugin
Version:        2.8.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-urdf_parser_plugin and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-urdf_parser_plugin
Requires:       ros2-iron-urdf_parser_plugin-devel

Obsoletes: ros-iron-urdf-parser-plugin < 2.8.2-1

%description
This package contains a C++ base class for URDF parsers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.2-1
- Update to latest release
