# Meta Package
Name:           ros-jazzy-moveit-planners-chomp
Version:        2.12.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-moveit_planners_chomp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_planners_chomp
Requires:       ros2-jazzy-moveit_planners_chomp-devel

Obsoletes: ros-jazzy-moveit-planners-chomp < 2.12.2-1

%description
The interface for using CHOMP within MoveIt

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.12.2-1
- Update to latest release
