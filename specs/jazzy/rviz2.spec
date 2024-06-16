# Meta Package
Name:           ros-jazzy-rviz2
Version:        14.1.1
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/ros2/rviz/blob/ros2/README.md
Summary:        Meta package for ros2-jazzy-rviz2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz2
Requires:       ros2-jazzy-rviz2-devel

Obsoletes: ros-jazzy-rviz2 < 14.1.1-1

%description
3D visualization tool for ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.0-1
- Update to latest release
