# Meta Package
Name:           ros-humble-realtime-tools
Version:        2.5.0
Release:        1%{?dist}
License:        3-Clause BSD
URL:            http://ros.org/wiki/realtime_tools
Summary:        Meta package for ros2-humble-realtime_tools and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-realtime_tools
Requires:       ros2-humble-realtime_tools-devel

Obsoletes: ros-humble-realtime-tools < 2.5.0-1

%description
Contains a set of tools that can be used from a hard realtime thread,
without breaking the realtime behavior.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.0-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.0-1
- update to latest release
