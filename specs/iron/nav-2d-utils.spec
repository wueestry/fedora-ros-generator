# Meta Package
Name:           ros-iron-nav-2d-utils
Version:        1.2.7
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav_2d_utils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav_2d_utils
Requires:       ros2-iron-nav_2d_utils-devel

Obsoletes: ros-iron-nav-2d-utils < 1.2.7-1

%description
A handful of useful utility functions for nav_2d packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
