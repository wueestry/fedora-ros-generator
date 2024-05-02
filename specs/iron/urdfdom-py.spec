# Meta Package
Name:           ros-iron-urdfdom-py
Version:        1.2.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/urdfdom_py
Summary:        Meta package for ros2-iron-urdfdom_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-urdfdom_py
Requires:       ros2-iron-urdfdom_py-devel

Obsoletes: ros-iron-urdfdom-py < 1.2.1-1

%description
Python implementation of the URDF parser.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.1-1
- Update to latest release
