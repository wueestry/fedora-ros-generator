# Meta Package
Name:           ros-humble-moveit-setup-srdf-plugins
Version:        2.5.5
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-moveit_setup_srdf_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-moveit_setup_srdf_plugins
Requires:       ros2-humble-moveit_setup_srdf_plugins-devel

Obsoletes: ros-humble-moveit-setup-srdf-plugins < 2.5.5-1

%description
SRDF-based plugins for MoveIt Setup Assistant

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
