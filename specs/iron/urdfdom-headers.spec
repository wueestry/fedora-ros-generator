# Meta Package
Name:           ros-iron-urdfdom-headers
Version:        1.1.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/urdf
Summary:        Meta package for ros2-iron-urdfdom_headers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-urdfdom_headers
Requires:       ros2-iron-urdfdom_headers-devel

Obsoletes: ros-iron-urdfdom-headers < 1.1.0-1

%description
C++ headers for URDF.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.1.0-1
- Update to latest release
