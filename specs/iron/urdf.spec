# Meta Package
Name:           ros-iron-urdf
Version:        2.8.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-urdf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-urdf
Requires:       ros2-iron-urdf-devel

Obsoletes: ros-iron-urdf < 2.8.2-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.2-1
- Update to latest release
