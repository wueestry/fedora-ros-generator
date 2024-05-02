# Meta Package
Name:           ros-humble-eigen-stl-containers
Version:        1.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-eigen_stl_containers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-eigen_stl_containers
Requires:       ros2-humble-eigen_stl_containers-devel

Obsoletes: ros-humble-eigen-stl-containers < 1.0.0-1

%description
This package provides a set of typedef's that allow using Eigen
datatypes in STL containers

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.0-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.0-1
- Initial humble build
