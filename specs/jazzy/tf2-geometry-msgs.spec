# Meta Package
Name:           ros-jazzy-tf2-geometry-msgs
Version:        0.36.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/tf2_ros
Summary:        Meta package for ros2-jazzy-tf2_geometry_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tf2_geometry_msgs
Requires:       ros2-jazzy-tf2_geometry_msgs-devel

Obsoletes: ros-jazzy-tf2-geometry-msgs < 0.36.2-1

%description
tf2_geometry_msgs

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.2-1
- Update to latest release
