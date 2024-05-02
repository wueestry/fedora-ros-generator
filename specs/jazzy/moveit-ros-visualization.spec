# Meta Package
Name:           ros-jazzy-moveit-ros-visualization
Version:        2.9.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_ros_visualization and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_ros_visualization
Requires:       ros2-jazzy-moveit_ros_visualization-devel

Obsoletes: ros-jazzy-moveit-ros-visualization < 2.9.0-1

%description
Components of MoveIt that offer visualization

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.9.0-1
- Update to latest release
