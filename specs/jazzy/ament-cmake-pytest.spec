# Meta Package
Name:           ros-jazzy-ament-cmake-pytest
Version:        2.5.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_pytest and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_pytest
Requires:       ros2-jazzy-ament_cmake_pytest-devel

Obsoletes: ros-jazzy-ament-cmake-pytest < 2.5.0-1

%description
The ability to run Python tests using pytest in the ament buildsystem
in CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.0-1
- Update to latest release
