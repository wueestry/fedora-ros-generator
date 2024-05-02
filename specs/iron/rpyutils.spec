# Meta Package
Name:           ros-iron-rpyutils
Version:        0.3.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rpyutils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rpyutils
Requires:       ros2-iron-rpyutils-devel

Obsoletes: ros-iron-rpyutils < 0.3.2-1

%description
Package containing various utility types and functions for Python

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.3.2-1
- Update to latest release
