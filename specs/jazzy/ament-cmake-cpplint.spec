# Meta Package
Name:           ros-jazzy-ament-cmake-cpplint
Version:        0.17.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_cpplint and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_cpplint
Requires:       ros2-jazzy-ament_cmake_cpplint-devel

Obsoletes: ros-jazzy-ament-cmake-cpplint < 0.17.2-1

%description
The CMake API for ament_cpplint to lint C / C++ code using cpplint.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
