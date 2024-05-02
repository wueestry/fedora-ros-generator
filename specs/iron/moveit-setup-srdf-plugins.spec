# Meta Package
Name:           ros-iron-moveit-setup-srdf-plugins
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-moveit_setup_srdf_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_setup_srdf_plugins
Requires:       ros2-iron-moveit_setup_srdf_plugins-devel

Obsoletes: ros-iron-moveit-setup-srdf-plugins < 2.8.0-1

%description
SRDF-based plugins for MoveIt Setup Assistant

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
