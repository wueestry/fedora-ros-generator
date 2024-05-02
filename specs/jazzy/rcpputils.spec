# Meta Package
Name:           ros-jazzy-rcpputils
Version:        2.11.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcpputils and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcpputils
Requires:       ros2-jazzy-rcpputils-devel

Obsoletes: ros-jazzy-rcpputils < 2.11.0-1

%description
Package containing utility code for C++.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.11.0-1
- Update to latest release
