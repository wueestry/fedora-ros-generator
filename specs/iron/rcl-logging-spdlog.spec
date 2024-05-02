# Meta Package
Name:           ros-iron-rcl-logging-spdlog
Version:        2.5.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rcl_logging_spdlog and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rcl_logging_spdlog
Requires:       ros2-iron-rcl_logging_spdlog-devel

Obsoletes: ros-iron-rcl-logging-spdlog < 2.5.1-1

%description
Implementation of rcl_logging API for an spdlog backend.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.5.1-1
- Update to latest release
