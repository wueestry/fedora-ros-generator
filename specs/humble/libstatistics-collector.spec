# Meta Package
Name:           ros-humble-libstatistics-collector
Version:        1.3.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-libstatistics_collector and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-libstatistics_collector
Requires:       ros2-humble-libstatistics_collector-devel

Obsoletes: ros-humble-libstatistics-collector < 1.3.2-1

%description
Lightweight aggregation utilities to collect statistics and measure
message metrics.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.2-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.1-1
- Initial humble build
