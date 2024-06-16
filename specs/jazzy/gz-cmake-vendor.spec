# Meta Package
Name:           ros-jazzy-gz-cmake-vendor
Version:        0.0.8
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-cmake
Summary:        Meta package for ros2-jazzy-gz_cmake_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_cmake_vendor
Requires:       ros2-jazzy-gz_cmake_vendor-devel

Obsoletes: ros-jazzy-gz-cmake-vendor < 0.0.8-1

%description
Vendor package for: gz-cmake3 3.5.3 Gazebo CMake : CMake Modules for
Gazebo Projects

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.8-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.7-1
- Update to latest release
