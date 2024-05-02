# Meta Package
Name:           ros-humble-urdf
Version:        2.6.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-urdf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-urdf
Requires:       ros2-humble-urdf-devel

Obsoletes: ros-humble-urdf < 2.6.0-1

%description
This package contains a C++ parser for the Unified Robot Description
Format (URDF), which is an XML format for representing a robot model.
The code API of the parser has been through our review process and
will remain backwards compatible in future releases.

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
