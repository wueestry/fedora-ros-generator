# Meta Package
Name:           ros-humble-ament-cmake-core
Version:        1.3.9
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ament_cmake_core and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ament_cmake_core
Requires:       ros2-humble-ament_cmake_core-devel

Obsoletes: ros-humble-ament-cmake-core < 1.3.9-1

%description
The core of the ament buildsystem in CMake. Several subcomponents
provide specific funtionalities: * environment: provide prefix-level
setup files * environment_hooks: provide package-level setup files and
environment hooks * index: store information in an index and retrieve
them without crawling * package_templates: templates from the
ament_package Python package * symlink_install: use symlinks for CMake
install commands

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
