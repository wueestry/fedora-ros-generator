# Meta Package
Name:           ros-jazzy-statistics-msgs
Version:        2.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-statistics_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-statistics_msgs
Requires:       ros2-jazzy-statistics_msgs-devel

Obsoletes: ros-jazzy-statistics-msgs < 2.0.2-1

%description
Message definitions for reporting statistics for topics and system
resources.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.2-1
- Update to latest release
