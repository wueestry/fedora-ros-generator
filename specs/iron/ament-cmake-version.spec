# Meta Package
Name:           ros-iron-ament-cmake-version
Version:        2.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_cmake_version and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_cmake_version
Requires:       ros2-iron-ament_cmake_version-devel

Obsoletes: ros-iron-ament-cmake-version < 2.0.5-1

%description
The ability to override the exported package version in the ament
buildsystem.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.5-1
- Update to latest release
