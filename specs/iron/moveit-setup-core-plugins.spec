# Meta Package
Name:           ros-iron-moveit-setup-core-plugins
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-moveit_setup_core_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_setup_core_plugins
Requires:       ros2-iron-moveit_setup_core_plugins-devel

Obsoletes: ros-iron-moveit-setup-core-plugins < 2.8.0-1

%description
Core (meta) plugins for MoveIt Setup Assistant

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
