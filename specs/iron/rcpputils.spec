# Meta Package
Name:           ros-iron-rcpputils
Version:        2.6.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rcpputils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rcpputils
Requires:       ros2-iron-rcpputils-devel

Obsoletes: ros-iron-rcpputils < 2.6.3-1

%description
Package containing utility code for C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.6.3-1
- Update to latest release
