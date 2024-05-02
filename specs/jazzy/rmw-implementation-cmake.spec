# Meta Package
Name:           ros-jazzy-rmw-implementation-cmake
Version:        7.3.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw_implementation_cmake and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw_implementation_cmake
Requires:       ros2-jazzy-rmw_implementation_cmake-devel

Obsoletes: ros-jazzy-rmw-implementation-cmake < 7.3.1-1

%description
CMake functions which can discover and enumerate available
implementations.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.7.3.1-1
- Update to latest release
