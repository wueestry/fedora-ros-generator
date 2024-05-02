# Meta Package
Name:           ros-jazzy-map-msgs
Version:        2.4.1
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/map_msgs
Summary:        Meta package for ros2-jazzy-map_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-map_msgs
Requires:       ros2-jazzy-map_msgs-devel

Obsoletes: ros-jazzy-map-msgs < 2.4.1-1

%description
This package defines messages commonly used in mapping packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.4.1-1
- Update to latest release
