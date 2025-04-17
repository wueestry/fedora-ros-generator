# Meta Package
Name:           ros-jazzy-sros2-cmake
Version:        0.13.3
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-sros2_cmake and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-sros2_cmake
Requires:       ros2-jazzy-sros2_cmake-devel

Obsoletes: ros-jazzy-sros2-cmake < 0.13.3-1

%description
CMake macros to configure security

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.13.3-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.13.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.13.0-1
- Update to latest release
