# Meta Package
Name:           ros-iron-eigen-stl-containers
Version:        1.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-eigen_stl_containers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-eigen_stl_containers
Requires:       ros2-iron-eigen_stl_containers-devel

Obsoletes: ros-iron-eigen-stl-containers < 1.0.0-1

%description
This package provides a set of typedef's that allow using Eigen
datatypes in STL containers

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.0-1
- Update to latest release
