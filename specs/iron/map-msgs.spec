# Meta Package
Name:           ros-iron-map-msgs
Version:        2.2.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/map_msgs
Summary:        Meta package for ros2-iron-map_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-map_msgs
Requires:       ros2-iron-map_msgs-devel

Obsoletes: ros-iron-map-msgs < 2.2.0-1

%description
This package defines messages commonly used in mapping packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.2.0-1
- Update to latest release
