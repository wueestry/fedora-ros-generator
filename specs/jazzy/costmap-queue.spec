# Meta Package
Name:           ros-jazzy-costmap-queue
Version:        1.3.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-costmap_queue and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-costmap_queue
Requires:       ros2-jazzy-costmap_queue-devel

Obsoletes: ros-jazzy-costmap-queue < 1.3.2-1

%description
The costmap_queue package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
