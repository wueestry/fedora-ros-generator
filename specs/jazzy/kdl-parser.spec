# Meta Package
Name:           ros-jazzy-kdl-parser
Version:        2.11.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-kdl_parser and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-kdl_parser
Requires:       ros2-jazzy-kdl_parser-devel

Obsoletes: ros-jazzy-kdl-parser < 2.11.0-1

%description
The Kinematics and Dynamics Library (KDL) defines a tree structure to
represent the kinematic and dynamic parameters of a robot mechanism.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.11.0-1
- Update to latest release
