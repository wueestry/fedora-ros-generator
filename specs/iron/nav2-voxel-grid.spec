# Meta Package
Name:           ros-iron-nav2-voxel-grid
Version:        1.2.7
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav2_voxel_grid and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav2_voxel_grid
Requires:       ros2-iron-nav2_voxel_grid-devel

Obsoletes: ros-iron-nav2-voxel-grid < 1.2.7-1

%description
voxel_grid provides an implementation of an efficient 3D voxel grid.
The occupancy grid can support 3 different representations for the
state of a cell: marked, free, or unknown. Due to the underlying
implementation relying on bitwise and and or integer operations, the
voxel grid only supports 16 different levels per voxel column.
However, this limitation yields raytracing and cell marking
performance in the grid comparable to standard 2D structures making it
quite fast compared to most 3D structures.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
