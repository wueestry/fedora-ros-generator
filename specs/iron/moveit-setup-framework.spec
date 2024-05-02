# Meta Package
Name:           ros-iron-moveit-setup-framework
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-moveit_setup_framework and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_setup_framework
Requires:       ros2-iron-moveit_setup_framework-devel

Obsoletes: ros-iron-moveit-setup-framework < 2.8.0-1

%description
C++ Interface for defining setup steps for MoveIt Setup Assistant

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
