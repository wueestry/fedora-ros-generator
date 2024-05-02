# Meta Package
Name:           ros-jazzy-tracetools
Version:        8.2.0
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://docs.ros.org/en/rolling/p/tracetools/
Summary:        Meta package for ros2-jazzy-tracetools and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tracetools
Requires:       ros2-jazzy-tracetools-devel

Obsoletes: ros-jazzy-tracetools < 8.2.0-1

%description
Tracing wrapper for ROS 2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.8.2.0-1
- Update to latest release
