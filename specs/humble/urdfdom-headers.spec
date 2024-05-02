# Meta Package
Name:           ros-humble-urdfdom-headers
Version:        1.0.6
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/urdf
Summary:        Meta package for ros2-humble-urdfdom_headers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-urdfdom_headers
Requires:       ros2-humble-urdfdom_headers-devel

Obsoletes: ros-humble-urdfdom-headers < 1.0.6-1

%description
C++ headers for URDF.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.6-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.6-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.6-1
- Initial humble build
