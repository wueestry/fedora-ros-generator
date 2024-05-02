# Meta Package
Name:           ros-iron-python-cmake-module
Version:        0.10.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-python_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-python_cmake_module
Requires:       ros2-iron-python_cmake_module-devel

Obsoletes: ros-iron-python-cmake-module < 0.10.2-1

%description
Provide CMake module with extra functionality for Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.10.2-1
- Update to latest release
