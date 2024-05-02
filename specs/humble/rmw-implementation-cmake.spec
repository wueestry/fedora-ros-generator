# Meta Package
Name:           ros-humble-rmw-implementation-cmake
Version:        6.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rmw_implementation_cmake and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rmw_implementation_cmake
Requires:       ros2-humble-rmw_implementation_cmake-devel

Obsoletes: ros-humble-rmw-implementation-cmake < 6.1.1-1

%description
CMake functions which can discover and enumerate available
implementations.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.1.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.1.1-1
- Initial humble build
