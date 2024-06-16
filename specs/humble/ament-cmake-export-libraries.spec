# Meta Package
Name:           ros-humble-ament-cmake-export-libraries
Version:        1.3.9
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ament_cmake_export_libraries and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ament_cmake_export_libraries
Requires:       ros2-humble-ament_cmake_export_libraries-devel

Obsoletes: ros-humble-ament-cmake-export-libraries < 1.3.9-1

%description
The ability to export libraries to downstream packages in the ament
buildsystem in CMake.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.9-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.8-1
- Update to latest release
* Mon Feb 12 2024 Tarik Viehmann - humble.1.3.7-1
- update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.6-1
- update to latest upstream
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.5-1
- update to latest upstream release
* Thu Jun 29 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.5-1
- update to latest upstream release
* Mon Jun 19 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.4-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.3-1
- Initial humble build
