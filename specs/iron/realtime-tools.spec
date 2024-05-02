# Meta Package
Name:           ros-iron-realtime-tools
Version:        2.5.0
Release:        1%{?dist}
License:        3-Clause BSD
URL:            http://ros.org/wiki/realtime_tools
Summary:        Meta package for ros2-iron-realtime_tools and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-realtime_tools
Requires:       ros2-iron-realtime_tools-devel

Obsoletes: ros-iron-realtime-tools < 2.5.0-1

%description
Contains a set of tools that can be used from a hard realtime thread,
without breaking the realtime behavior.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.5.0-1
- Update to latest release
