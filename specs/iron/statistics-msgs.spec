# Meta Package
Name:           ros-iron-statistics-msgs
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-statistics_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-statistics_msgs
Requires:       ros2-iron-statistics_msgs-devel

Obsoletes: ros-iron-statistics-msgs < 1.6.0-1

%description
Message definitions for reporting statistics for topics and system
resources.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.0-1
- Update to latest release
