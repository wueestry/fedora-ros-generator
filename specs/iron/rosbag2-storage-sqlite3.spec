# Meta Package
Name:           ros-iron-rosbag2-storage-sqlite3
Version:        0.22.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosbag2_storage_sqlite3 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosbag2_storage_sqlite3
Requires:       ros2-iron-rosbag2_storage_sqlite3-devel

Obsoletes: ros-iron-rosbag2-storage-sqlite3 < 0.22.6-1

%description
ROSBag2 SQLite3 storage plugin

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest release
