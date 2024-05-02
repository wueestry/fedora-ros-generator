# Meta Package
Name:           ros-jazzy-urdfdom-headers
Version:        1.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/urdf
Summary:        Meta package for ros2-jazzy-urdfdom_headers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-urdfdom_headers
Requires:       ros2-jazzy-urdfdom_headers-devel

Obsoletes: ros-jazzy-urdfdom-headers < 1.1.1-1

%description
C++ headers for URDF.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.1.1-1
- Update to latest release
