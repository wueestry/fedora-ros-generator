# Meta Package
Name:           ros-jazzy-ament-cmake-export-interfaces
Version:        2.5.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_export_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_export_interfaces
Requires:       ros2-jazzy-ament_cmake_export_interfaces-devel

Obsoletes: ros-jazzy-ament-cmake-export-interfaces < 2.5.2-1

%description
The ability to export interfaces to downstream packages in the ament
buildsystem in CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.0-1
- Update to latest release
