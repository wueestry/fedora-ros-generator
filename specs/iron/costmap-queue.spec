# Meta Package
Name:           ros-iron-costmap-queue
Version:        1.2.7
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-costmap_queue and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-costmap_queue
Requires:       ros2-iron-costmap_queue-devel

Obsoletes: ros-iron-costmap-queue < 1.2.7-1

%description
The costmap_queue package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
