# Meta Package
Name:           ros-humble-sqlite3-vendor
Version:        0.15.11
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-sqlite3_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-sqlite3_vendor
Requires:       ros2-humble-sqlite3_vendor-devel

Obsoletes: ros-humble-sqlite3-vendor < 0.15.11-1

%description
SQLite 3 vendor package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.11-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.9-1
- Update to latest release
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.8-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.7-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.7-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.7-1
- update to latest upstream
* Fri Jun 30 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.15.6-1
- update to latest upstream release
