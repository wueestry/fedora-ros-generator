# Meta Package
Name:           ros-jazzy-ament-cmake-uncrustify
Version:        0.17.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_cmake_uncrustify and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_cmake_uncrustify
Requires:       ros2-jazzy-ament_cmake_uncrustify-devel

Obsoletes: ros-jazzy-ament-cmake-uncrustify < 0.17.1-1

%description
The CMake API for ament_uncrustify to check code against
styleconventions using uncrustify.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
