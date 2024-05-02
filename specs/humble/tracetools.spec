# Meta Package
Name:           ros-humble-tracetools
Version:        4.1.1
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://index.ros.org/p/tracetools/
Summary:        Meta package for ros2-humble-tracetools and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tracetools
Requires:       ros2-humble-tracetools-devel

Obsoletes: ros-humble-tracetools < 4.1.1-1

%description
Tracing wrapper for ROS 2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.1.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.1.1-1
- Initial humble build
