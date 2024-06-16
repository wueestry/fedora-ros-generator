# Meta Package
Name:           ros-humble-logging-demo
Version:        0.20.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-logging_demo and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-logging_demo
Requires:       ros2-humble-logging_demo-devel

Obsoletes: ros-humble-logging-demo < 0.20.4-1

%description
Examples for using and configuring loggers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.4-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- Initial humble build
