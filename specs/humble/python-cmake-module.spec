# Meta Package
Name:           ros-humble-python-cmake-module
Version:        0.10.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-python_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-python_cmake_module
Requires:       ros2-humble-python_cmake_module-devel

Obsoletes: ros-humble-python-cmake-module < 0.10.0-1

%description
Provide CMake module with extra functionality for Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- Initial humble build
