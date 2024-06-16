# Meta Package
Name:           ros-humble-nav2-voxel-grid
Version:        1.1.15
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-nav2_voxel_grid and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-nav2_voxel_grid
Requires:       ros2-humble-nav2_voxel_grid-devel

Obsoletes: ros-humble-nav2-voxel-grid < 1.1.15-1

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
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.15-1
- Update to latest release
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.14-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.13-1
- Update to latest release
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.12-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.9-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.9-1
- update to latest upstream release
* Wed Aug 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.9-1
- update to latest upstream
* Fri Jun 30 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.8-1
- update to latest upstream release
* Mon Jun 19 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.7-1
- update to latest release
* Mon Apr 10 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.6-1
- update to latest upsteam
