# Meta Package
Name:           ros-jazzy-python-cmake-module
Version:        0.11.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-python_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-python_cmake_module
Requires:       ros2-jazzy-python_cmake_module-devel

Obsoletes: ros-jazzy-python-cmake-module < 0.11.1-1

%description
Provide CMake module with extra functionality for Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.11.1-1
- Update to latest release
