# Meta Package
Name:           ros-iron-sros2-cmake
Version:        0.11.3
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-sros2_cmake and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-sros2_cmake
Requires:       ros2-iron-sros2_cmake-devel

Obsoletes: ros-iron-sros2-cmake < 0.11.3-1

%description
CMake macros to configure security

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.11.3-1
- Update to latest release
