# Meta Package
Name:           ros-humble-fastrtps-cmake-module
Version:        2.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-fastrtps_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-fastrtps_cmake_module
Requires:       ros2-humble-fastrtps_cmake_module-devel

Obsoletes: ros-humble-fastrtps-cmake-module < 2.2.2-1

%description
Provide CMake module to find eProsima FastRTPS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.2-1
- update to latest upstream
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.1-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.1-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.0-1
- Initial humble build
