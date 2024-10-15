# Meta Package
Name:           ros-jazzy-ament-cmake-clang-format
Version:        0.17.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_clang_format and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_clang_format
Requires:       ros2-jazzy-ament_cmake_clang_format-devel

Obsoletes: ros-jazzy-ament-cmake-clang-format < 0.17.1-1

%description
The CMake API for ament_clang_format to lint C / C++ code using clang
format.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
