# Meta Package
Name:           ros-iron-dwb-critics
Version:        1.2.7
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-dwb_critics and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-dwb_critics
Requires:       ros2-iron-dwb_critics-devel

Obsoletes: ros-iron-dwb-critics < 1.2.7-1

%description
The dwb_critics package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
