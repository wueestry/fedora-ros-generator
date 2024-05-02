# Meta Package
Name:           ros-humble-urdf-parser-plugin
Version:        2.6.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-urdf_parser_plugin and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-urdf_parser_plugin
Requires:       ros2-humble-urdf_parser_plugin-devel

Obsoletes: ros-humble-urdf-parser-plugin < 2.6.0-1

%description
This package contains a C++ base class for URDF parsers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.13.2-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.0-1
- Initial humble build
