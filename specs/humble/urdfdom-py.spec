# Meta Package
Name:           ros-humble-urdfdom-py
Version:        1.2.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/urdfdom_py
Summary:        Meta package for ros2-humble-urdfdom_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-urdfdom_py
Requires:       ros2-humble-urdfdom_py-devel

Obsoletes: ros-humble-urdfdom-py < 1.2.1-1

%description
Python implementation of the URDF parser.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.1-1
- update to latest release
* Fri Aug 11 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.1-1
- update to latest upstream
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- Initial humble build
