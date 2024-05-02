# Meta Package
Name:           ros-jazzy-ament-index-cpp
Version:        1.8.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_index_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_index_cpp
Requires:       ros2-jazzy-ament_index_cpp-devel

Obsoletes: ros-jazzy-ament-index-cpp < 1.8.1-1

%description
C++ API to access the ament resource index.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.8.1-1
- Update to latest release
