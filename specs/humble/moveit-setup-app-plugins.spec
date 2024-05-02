# Meta Package
Name:           ros-humble-moveit-setup-app-plugins
Version:        2.5.5
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-moveit_setup_app_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-moveit_setup_app_plugins
Requires:       ros2-humble-moveit_setup_app_plugins-devel

Obsoletes: ros-humble-moveit-setup-app-plugins < 2.5.5-1

%description
Various specialty plugins for MoveIt Setup Assistant

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.5-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.4-1
- Initial humble build
