# Meta Package
Name:           ros-humble-eigen3-cmake-module
Version:        0.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-eigen3_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-eigen3_cmake_module
Requires:       ros2-humble-eigen3_cmake_module-devel

Obsoletes: ros-humble-eigen3-cmake-module < 0.1.1-1

%description
Exports a custom CMake module to find Eigen3.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- Initial humble build
