# Meta Package
Name:           ros-jazzy-diagnostic-updater
Version:        4.2.3
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/wiki/diagnostic_updater
Summary:        Meta package for ros2-jazzy-diagnostic_updater and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-diagnostic_updater
Requires:       ros2-jazzy-diagnostic_updater-devel

Obsoletes: ros-jazzy-diagnostic-updater < 4.2.3-1

%description
diagnostic_updater contains tools for easily updating diagnostics. it
is commonly used in device drivers to keep track of the status of
output topics, device status, etc.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 10 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.2.3-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.2.2-1
- Update to latest release
* Thu Aug 01 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.2.1-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.2.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.2-1
- Update to latest release
