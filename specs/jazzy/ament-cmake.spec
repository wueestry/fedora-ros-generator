# Meta Package
Name:           ros-jazzy-ament-cmake
Version:        2.5.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake
Requires:       ros2-jazzy-ament_cmake-devel

Obsoletes: ros-jazzy-ament-cmake < 2.5.0-1

%description
The entry point package for the ament buildsystem in CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.0-1
- Update to latest release
