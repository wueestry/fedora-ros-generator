# Meta Package
Name:           ros-jazzy-ur-moveit-config
Version:        3.2.0
Release:        1%{?dist}
License:        Apache2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ur_moveit_config and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ur_moveit_config
Requires:       ros2-jazzy-ur_moveit_config-devel

Obsoletes: ros-jazzy-ur-moveit-config < 3.2.0-1

%description
An example package with MoveIt2 configurations for UR robots.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.2.0-1
- Update to latest release
