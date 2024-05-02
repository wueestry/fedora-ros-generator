# Meta Package
Name:           ros-humble-rcl-logging-spdlog
Version:        2.3.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rcl_logging_spdlog and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rcl_logging_spdlog
Requires:       ros2-humble-rcl_logging_spdlog-devel

Obsoletes: ros-humble-rcl-logging-spdlog < 2.3.1-1

%description
Implementation of rcl_logging API for an spdlog backend.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.1-1
- Initial humble build
