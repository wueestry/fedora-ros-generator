# Meta Package
Name:           ros-humble-pcl-ros
Version:        2.4.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/perception_pcl
Summary:        Meta package for ros2-humble-pcl_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-pcl_ros
Requires:       ros2-humble-pcl_ros-devel

Obsoletes: ros-humble-pcl-ros < 2.4.0-1

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
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.0-1
- Update to latest release
