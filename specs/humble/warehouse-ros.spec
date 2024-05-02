# Meta Package
Name:           ros-humble-warehouse-ros
Version:        2.0.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-warehouse_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-warehouse_ros
Requires:       ros2-humble-warehouse_ros-devel

Obsoletes: ros-humble-warehouse-ros < 2.0.4-1

%description
Persistent storage of ROS messages

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.4-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.4-1
- Initial humble build
