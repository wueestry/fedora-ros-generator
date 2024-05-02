# Meta Package
Name:           ros-iron-tracetools
Version:        6.3.1
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://index.ros.org/p/tracetools/
Summary:        Meta package for ros2-iron-tracetools and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tracetools
Requires:       ros2-iron-tracetools-devel

Obsoletes: ros-iron-tracetools < 6.3.1-1

%description
Tracing wrapper for ROS 2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.6.3.1-1
- Update to latest release
