# Meta Package
Name:           ros-iron-ament-cmake-export-targets
Version:        2.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_cmake_export_targets and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_cmake_export_targets
Requires:       ros2-iron-ament_cmake_export_targets-devel

Obsoletes: ros-iron-ament-cmake-export-targets < 2.0.5-1

%description
The ability to export targets to downstream packages in the ament
buildsystem in CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.5-1
- Update to latest release
