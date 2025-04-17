# Meta Package
Name:           ros-jazzy-warehouse-ros-sqlite
Version:        1.0.5
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-warehouse_ros_sqlite and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-warehouse_ros_sqlite
Requires:       ros2-jazzy-warehouse_ros_sqlite-devel

Obsoletes: ros-jazzy-warehouse-ros-sqlite < 1.0.5-1

%description
Implementation of warehouse_ros for sqlite

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.5-1
- Update to latest release
