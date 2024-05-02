# Meta Package
Name:           ros-iron-eigen3-cmake-module
Version:        0.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-eigen3_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-eigen3_cmake_module
Requires:       ros2-iron-eigen3_cmake_module-devel

Obsoletes: ros-iron-eigen3-cmake-module < 0.2.2-1

%description
Exports a custom CMake module to find Eigen3.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.2.2-1
- Update to latest release
