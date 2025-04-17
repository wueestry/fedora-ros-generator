# Meta Package
Name:           ros-jazzy-realtime-tools
Version:        3.5.0
Release:        1%{?dist}
License:        3-Clause BSD
URL:            https://control.ros.org
Summary:        Meta package for ros2-jazzy-realtime_tools and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-realtime_tools
Requires:       ros2-jazzy-realtime_tools-devel

Obsoletes: ros-jazzy-realtime-tools < 3.5.0-1

%description
Contains a set of tools that can be used from a hard realtime thread,
without breaking the realtime behavior.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 10 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.5.0-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.0-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.0-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.8.1-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.6.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.0-1
- Update to latest release
