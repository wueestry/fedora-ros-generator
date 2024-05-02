# Meta Package
Name:           ros-humble-moveit-ros-warehouse
Version:        2.5.5
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-humble-moveit_ros_warehouse and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-moveit_ros_warehouse
Requires:       ros2-humble-moveit_ros_warehouse-devel

Obsoletes: ros-humble-moveit-ros-warehouse < 2.5.5-1

%description
Components of MoveIt connecting to MongoDB

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.5-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.4-1
- Initial humble build
