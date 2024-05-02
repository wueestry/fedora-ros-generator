# Meta Package
Name:           ros-jazzy-rcutils
Version:        6.7.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcutils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcutils
Requires:       ros2-jazzy-rcutils-devel

Obsoletes: ros-jazzy-rcutils < 6.7.1-1

%description
Package containing various utility types and functions for C

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.6.7.1-1
- Update to latest release
