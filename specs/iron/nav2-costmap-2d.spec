# Meta Package
Name:           ros-iron-nav2-costmap-2d
Version:        1.2.7
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav2_costmap_2d and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav2_costmap_2d
Requires:       ros2-iron-nav2_costmap_2d-devel

Obsoletes: ros-iron-nav2-costmap-2d < 1.2.7-1

%description
This package provides an implementation of a 2D costmap that takes in
sensor data from the world, builds a 2D or 3D occupancy grid of the
data (depending on whether a voxel based implementation is used), and
inflates costs in a 2D costmap based on the occupancy grid and a user
specified inflation radius. This package also provides support for
map_server based initialization of a costmap, rolling window based
costmaps, and parameter based subscription to and configuration of
sensor topics.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
