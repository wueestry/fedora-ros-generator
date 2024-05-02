# Meta Package
Name:           ros-iron-ament-index-cpp
Version:        1.5.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_index_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_index_cpp
Requires:       ros2-iron-ament_index_cpp-devel

Obsoletes: ros-iron-ament-index-cpp < 1.5.2-1

%description
C++ API to access the ament resource index.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.5.2-1
- Update to latest release
