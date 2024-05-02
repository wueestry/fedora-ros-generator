# Meta Package
Name:           ros-iron-rcutils
Version:        6.2.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rcutils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rcutils
Requires:       ros2-iron-rcutils-devel

Obsoletes: ros-iron-rcutils < 6.2.3-1

%description
Package containing various utility types and functions for C

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.6.2.3-1
- Update to latest release
