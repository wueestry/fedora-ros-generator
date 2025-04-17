# Meta Package
Name:           ros-jazzy-ros2-control-cmake
Version:        0.1.1
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros2_control_cmake and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros2_control_cmake
Requires:       ros2-jazzy-ros2_control_cmake-devel

Obsoletes: ros-jazzy-ros2-control-cmake < 0.1.1-1

%description
Provides CMake macros used by the ros2_control framework

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 10 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.1.1-1
- Update to latest release
