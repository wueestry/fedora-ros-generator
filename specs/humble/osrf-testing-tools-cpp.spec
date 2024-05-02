# Meta Package
Name:           ros-humble-osrf-testing-tools-cpp
Version:        1.5.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-osrf_testing_tools_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-osrf_testing_tools_cpp
Requires:       ros2-humble-osrf_testing_tools_cpp-devel

Obsoletes: ros-humble-osrf-testing-tools-cpp < 1.5.2-1

%description
Testing tools for C++, and is used in various OSRF projects.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.2-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.2-1
- Initial humble build
