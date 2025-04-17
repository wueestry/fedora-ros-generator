# Meta Package
Name:           ros-jazzy-plansys2-pddl-parser
Version:        2.0.18
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-plansys2_pddl_parser and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-plansys2_pddl_parser
Requires:       ros2-jazzy-plansys2_pddl_parser-devel

Obsoletes: ros-jazzy-plansys2-pddl-parser < 2.0.18-1

%description
This package contains a library for parsing PDDL domains and problems.
This package derives from the work of Anders Jonsson, contained in
https://github.com/wisdompoet/universal-pddl-parser.git with many
modifications by Francisco Martin: * ROS2 packaging * Source code
structure refactor * CMakeLists.txt for cmake compilation * Reading
from String instead of files * Licensing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.18-1
- Update to latest release
