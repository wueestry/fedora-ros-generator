# Meta Package
Name:           ros-jazzy-rviz-visual-tools
Version:        4.1.4
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/PickNikRobotics/rviz_visual_tools
Summary:        Meta package for ros2-jazzy-rviz_visual_tools and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz_visual_tools
Requires:       ros2-jazzy-rviz_visual_tools-devel

Obsoletes: ros-jazzy-rviz-visual-tools < 4.1.4-1

%description
Utility functions for displaying and debugging data in Rviz via
published markers

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.1.4-1
- Update to latest release
