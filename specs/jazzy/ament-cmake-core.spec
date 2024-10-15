# Meta Package
Name:           ros-jazzy-ament-cmake-core
Version:        2.5.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_core and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_core
Requires:       ros2-jazzy-ament_cmake_core-devel

Obsoletes: ros-jazzy-ament-cmake-core < 2.5.2-1

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
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.0-1
- Update to latest release
