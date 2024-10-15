# Meta Package
Name:           ros-jazzy-moveit-setup-app-plugins
Version:        2.10.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-moveit_setup_app_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_setup_app_plugins
Requires:       ros2-jazzy-moveit_setup_app_plugins-devel

Obsoletes: ros-jazzy-moveit-setup-app-plugins < 2.10.0-1

%description
Various specialty plugins for MoveIt Setup Assistant

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
