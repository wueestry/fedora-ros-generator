# Meta Package
Name:           ros-jazzy-sqlite3-vendor
Version:        0.26.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-sqlite3_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-sqlite3_vendor
Requires:       ros2-jazzy-sqlite3_vendor-devel

Obsoletes: ros-jazzy-sqlite3-vendor < 0.26.2-1

%description
SQLite 3 vendor package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.2-1
- Update to latest release
