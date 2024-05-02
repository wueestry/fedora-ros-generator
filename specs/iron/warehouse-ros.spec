# Meta Package
Name:           ros-iron-warehouse-ros
Version:        2.0.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-warehouse_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-warehouse_ros
Requires:       ros2-iron-warehouse_ros-devel

Obsoletes: ros-iron-warehouse-ros < 2.0.4-1

%description
Persistent storage of ROS messages

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.4-1
- Update to latest release
