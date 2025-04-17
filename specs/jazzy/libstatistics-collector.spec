# Meta Package
Name:           ros-jazzy-libstatistics-collector
Version:        1.7.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-libstatistics_collector and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-libstatistics_collector
Requires:       ros2-jazzy-libstatistics_collector-devel

Obsoletes: ros-jazzy-libstatistics-collector < 1.7.4-1

%description
Lightweight aggregation utilities to collect statistics and measure
message metrics.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.7.4-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.7.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.7.2-1
- Update to latest release
