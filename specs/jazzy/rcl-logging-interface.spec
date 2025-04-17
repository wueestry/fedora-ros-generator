# Meta Package
Name:           ros-jazzy-rcl-logging-interface
Version:        3.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcl_logging_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcl_logging_interface
Requires:       ros2-jazzy-rcl_logging_interface-devel

Obsoletes: ros-jazzy-rcl-logging-interface < 3.1.1-1

%description
Interface that rcl_logging backends needs to implement.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.0-1
- Update to latest release
