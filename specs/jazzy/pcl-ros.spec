# Meta Package
Name:           ros-jazzy-pcl-ros
Version:        2.6.1
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/perception_pcl
Summary:        Meta package for ros2-jazzy-pcl_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pcl_ros
Requires:       ros2-jazzy-pcl_ros-devel

Obsoletes: ros-jazzy-pcl-ros < 2.6.1-1

%description
PCL (Point Cloud Library) ROS interface stack. PCL-ROS is the
preferred bridge for 3D applications involving n-D Point Clouds and 3D
geometry processing in ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.6.1-1
- Update to latest release
