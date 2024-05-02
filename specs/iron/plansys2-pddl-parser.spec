# Meta Package
Name:           ros-iron-plansys2-pddl-parser
Version:        2.0.11
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-plansys2_pddl_parser and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-plansys2_pddl_parser
Requires:       ros2-iron-plansys2_pddl_parser-devel

Obsoletes: ros-iron-plansys2-pddl-parser < 2.0.11-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.11-1
- Update to latest release
