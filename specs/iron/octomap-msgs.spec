# Meta Package
Name:           ros-iron-octomap-msgs
Version:        2.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/octomap_msgs
Summary:        Meta package for ros2-iron-octomap_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-octomap_msgs
Requires:       ros2-iron-octomap_msgs-devel

Obsoletes: ros-iron-octomap-msgs < 2.0.0-1

%description
This package provides messages and serializations / conversion for the

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.0-1
- Update to latest release
