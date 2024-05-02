# Meta Package
Name:           ros-humble-moveit-simple-controller-manager
Version:        2.5.5
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-humble-moveit_simple_controller_manager and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-moveit_simple_controller_manager
Requires:       ros2-humble-moveit_simple_controller_manager-devel

Obsoletes: ros-humble-moveit-simple-controller-manager < 2.5.5-1

%description
A generic, simple controller manager plugin for MoveIt.

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
