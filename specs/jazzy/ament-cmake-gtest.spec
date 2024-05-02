# Meta Package
Name:           ros-jazzy-ament-cmake-gtest
Version:        2.5.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_gtest and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_gtest
Requires:       ros2-jazzy-ament_cmake_gtest-devel

Obsoletes: ros-jazzy-ament-cmake-gtest < 2.5.0-1

%description
The ability to add gtest-based tests in the ament buildsystem in
CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.0-1
- Update to latest release
