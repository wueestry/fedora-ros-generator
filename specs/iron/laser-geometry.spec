# Meta Package
Name:           ros-iron-laser-geometry
Version:        2.5.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-laser_geometry and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-laser_geometry
Requires:       ros2-iron-laser_geometry-devel

Obsoletes: ros-iron-laser-geometry < 2.5.0-1

%description
This package contains a class for converting from a 2D laser scan as
defined by sensor_msgs/LaserScan into a point cloud as defined by
sensor_msgs/PointCloud or sensor_msgs/PointCloud2. In particular, it
contains functionality to account for the skew resulting from moving
robots or tilting laser scanners.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.5.0-1
- Update to latest release
