# Meta Package
Name:           ros-jazzy-rcl-logging-spdlog
Version:        3.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcl_logging_spdlog and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcl_logging_spdlog
Requires:       ros2-jazzy-rcl_logging_spdlog-devel

Obsoletes: ros-jazzy-rcl-logging-spdlog < 3.1.0-1

%description
Implementation of rcl_logging API for an spdlog backend.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.0-1
- Update to latest release
