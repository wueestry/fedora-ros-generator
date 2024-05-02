# Meta Package
Name:           ros-iron-moveit-visual-tools
Version:        4.1.0
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/ros-planning/moveit_visual_tools
Summary:        Meta package for ros2-iron-moveit_visual_tools and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_visual_tools
Requires:       ros2-iron-moveit_visual_tools-devel

Obsoletes: ros-iron-moveit-visual-tools < 4.1.0-1

%description
Helper functions for displaying and debugging MoveIt data in Rviz via
published markers

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.1.0-1
- Update to latest release
