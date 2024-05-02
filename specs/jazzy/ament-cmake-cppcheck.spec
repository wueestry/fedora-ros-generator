# Meta Package
Name:           ros-jazzy-ament-cmake-cppcheck
Version:        0.17.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_cppcheck and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_cppcheck
Requires:       ros2-jazzy-ament_cmake_cppcheck-devel

Obsoletes: ros-jazzy-ament-cmake-cppcheck < 0.17.0-1

%description
The CMake API for ament_cppcheck to perform static code analysis on
C/C++ code using Cppcheck.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
