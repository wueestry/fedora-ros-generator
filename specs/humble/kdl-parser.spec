# Meta Package
Name:           ros-humble-kdl-parser
Version:        2.6.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-kdl_parser and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-kdl_parser
Requires:       ros2-humble-kdl_parser-devel

Obsoletes: ros-humble-kdl-parser < 2.6.4-1

%description
The Kinematics and Dynamics Library (KDL) defines a tree structure to
represent the kinematic and dynamic parameters of a robot mechanism.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.4-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.4-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.4-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.14.2-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.4-1
- Initial humble build
