# Meta Package
Name:           ros-jazzy-eigen-stl-containers
Version:        1.1.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-eigen_stl_containers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-eigen_stl_containers
Requires:       ros2-jazzy-eigen_stl_containers-devel

Obsoletes: ros-jazzy-eigen-stl-containers < 1.1.0-1

%description
This package provides a set of typedef's that allow using Eigen
datatypes in STL containers

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.1.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.0-1
- Update to latest release
