# Meta Package
Name:           ros-jazzy-moveit-setup-srdf-plugins
Version:        2.10.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-moveit_setup_srdf_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_setup_srdf_plugins
Requires:       ros2-jazzy-moveit_setup_srdf_plugins-devel

Obsoletes: ros-jazzy-moveit-setup-srdf-plugins < 2.10.0-1

%description
SRDF-based plugins for MoveIt Setup Assistant

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.10.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
