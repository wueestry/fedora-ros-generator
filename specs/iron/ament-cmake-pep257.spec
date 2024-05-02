# Meta Package
Name:           ros-iron-ament-cmake-pep257
Version:        0.14.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_cmake_pep257 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_cmake_pep257
Requires:       ros2-iron-ament_cmake_pep257-devel

Obsoletes: ros-iron-ament-cmake-pep257 < 0.14.3-1

%description
The CMake API for ament_pep257 to check code against the docstring
style conventions in PEP 257.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.14.3-1
- Update to latest release
