# Meta Package
Name:           ros-iron-pcl-conversions
Version:        2.5.3
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-pcl_conversions and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-pcl_conversions
Requires:       ros2-iron-pcl_conversions-devel

Obsoletes: ros-iron-pcl-conversions < 2.5.3-1

%description
Provides conversions from PCL data types and ROS message types

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.5.3-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.4.0-1
- Update to latest release
