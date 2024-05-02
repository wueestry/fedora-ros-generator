# Meta Package
Name:           ros-iron-libstatistics-collector
Version:        1.5.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-libstatistics_collector and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-libstatistics_collector
Requires:       ros2-iron-libstatistics_collector-devel

Obsoletes: ros-iron-libstatistics-collector < 1.5.2-1

%description
Lightweight aggregation utilities to collect statistics and measure
message metrics.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.5.2-1
- Update to latest release
