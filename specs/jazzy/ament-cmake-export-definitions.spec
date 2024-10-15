# Meta Package
Name:           ros-jazzy-ament-cmake-export-definitions
Version:        2.5.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_export_definitions and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_export_definitions
Requires:       ros2-jazzy-ament_cmake_export_definitions-devel

Obsoletes: ros-jazzy-ament-cmake-export-definitions < 2.5.2-1

%description
The ability to export definitions to downstream packages in the ament
buildsystem.

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
