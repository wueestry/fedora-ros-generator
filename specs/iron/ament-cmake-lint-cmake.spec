# Meta Package
Name:           ros-iron-ament-cmake-lint-cmake
Version:        0.14.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_cmake_lint_cmake and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_cmake_lint_cmake
Requires:       ros2-iron-ament_cmake_lint_cmake-devel

Obsoletes: ros-iron-ament-cmake-lint-cmake < 0.14.3-1

%description
The CMake API for ament_lint_cmake to lint CMake code using cmakelint.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.14.3-1
- Update to latest release
