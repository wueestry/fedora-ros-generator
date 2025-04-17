# Meta Package
Name:           ros-jazzy-pcl-conversions
Version:        2.6.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-pcl_conversions and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pcl_conversions
Requires:       ros2-jazzy-pcl_conversions-devel

Obsoletes: ros-jazzy-pcl-conversions < 2.6.2-1

%description
Provides conversions from PCL data types and ROS message types

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.6.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.6.1-1
- Update to latest release
