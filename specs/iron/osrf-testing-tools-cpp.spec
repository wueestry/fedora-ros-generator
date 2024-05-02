# Meta Package
Name:           ros-iron-osrf-testing-tools-cpp
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-osrf_testing_tools_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-osrf_testing_tools_cpp
Requires:       ros2-iron-osrf_testing_tools_cpp-devel

Obsoletes: ros-iron-osrf-testing-tools-cpp < 1.6.0-1

%description
Testing tools for C++, and is used in various OSRF projects.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.0-1
- Update to latest release
