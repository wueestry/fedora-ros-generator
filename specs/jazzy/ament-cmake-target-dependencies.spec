# Meta Package
Name:           ros-jazzy-ament-cmake-target-dependencies
Version:        2.5.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_target_dependencies and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_target_dependencies
Requires:       ros2-jazzy-ament_cmake_target_dependencies-devel

Obsoletes: ros-jazzy-ament-cmake-target-dependencies < 2.5.3-1

%description
The ability to add definitions, include directories and libraries of a
package to a target in the ament buildsystem in CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.3-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.0-1
- Update to latest release
