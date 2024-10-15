# Meta Package
Name:           ros-jazzy-dwb-core
Version:        1.3.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-dwb_core and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-dwb_core
Requires:       ros2-jazzy-dwb_core-devel

Obsoletes: ros-jazzy-dwb-core < 1.3.2-1

%description
DWB core interfaces package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
