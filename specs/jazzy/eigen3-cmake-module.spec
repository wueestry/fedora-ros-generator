# Meta Package
Name:           ros-jazzy-eigen3-cmake-module
Version:        0.3.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-eigen3_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-eigen3_cmake_module
Requires:       ros2-jazzy-eigen3_cmake_module-devel

Obsoletes: ros-jazzy-eigen3-cmake-module < 0.3.0-1

%description
Exports a custom CMake module to find Eigen3.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.3.0-1
- Update to latest release
