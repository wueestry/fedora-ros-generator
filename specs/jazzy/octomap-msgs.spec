# Meta Package
Name:           ros-jazzy-octomap-msgs
Version:        2.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/octomap_msgs
Summary:        Meta package for ros2-jazzy-octomap_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-octomap_msgs
Requires:       ros2-jazzy-octomap_msgs-devel

Obsoletes: ros-jazzy-octomap-msgs < 2.0.0-1

%description
This package provides messages and serializations / conversion for the

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.0-1
- Update to latest release
