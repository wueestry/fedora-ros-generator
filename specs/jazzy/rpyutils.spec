# Meta Package
Name:           ros-jazzy-rpyutils
Version:        0.4.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rpyutils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rpyutils
Requires:       ros2-jazzy-rpyutils-devel

Obsoletes: ros-jazzy-rpyutils < 0.4.1-1

%description
Package containing various utility types and functions for Python

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.4.1-1
- Update to latest release
