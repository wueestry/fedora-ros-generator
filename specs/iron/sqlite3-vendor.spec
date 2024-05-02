# Meta Package
Name:           ros-iron-sqlite3-vendor
Version:        0.22.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-sqlite3_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-sqlite3_vendor
Requires:       ros2-iron-sqlite3_vendor-devel

Obsoletes: ros-iron-sqlite3-vendor < 0.22.6-1

%description
SQLite 3 vendor package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest release
