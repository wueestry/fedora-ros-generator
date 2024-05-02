# Meta Package
Name:           ros-jazzy-webots-ros2-importer
Version:        2023.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-jazzy-webots_ros2_importer and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-webots_ros2_importer
Requires:       ros2-jazzy-webots_ros2_importer-devel

Obsoletes: ros-jazzy-webots-ros2-importer < 2023.1.2-1

%description
This package allows to convert URDF and XACRO files into Webots PROTO
files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2023.1.2-1
- Update to latest release
