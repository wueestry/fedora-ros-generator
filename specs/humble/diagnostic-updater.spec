# Meta Package
Name:           ros-humble-diagnostic-updater
Version:        3.1.2
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/wiki/diagnostic_updater
Summary:        Meta package for ros2-humble-diagnostic_updater and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-diagnostic_updater
Requires:       ros2-humble-diagnostic_updater-devel

Obsoletes: ros-humble-diagnostic-updater < 3.1.2-1

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
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.2-1
- update to latest upstream release
* Mon Apr 10 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.2-1
- update to latest upsteam
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.11.0-1
- update to latest release
