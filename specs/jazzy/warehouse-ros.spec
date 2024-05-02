# Meta Package
Name:           ros-jazzy-warehouse-ros
Version:        2.0.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-warehouse_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-warehouse_ros
Requires:       ros2-jazzy-warehouse_ros-devel

Obsoletes: ros-jazzy-warehouse-ros < 2.0.4-1

%description
Persistent storage of ROS messages

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.4-1
- Update to latest release
