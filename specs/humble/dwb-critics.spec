# Meta Package
Name:           ros-humble-dwb-critics
Version:        1.1.15
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-dwb_critics and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-dwb_critics
Requires:       ros2-humble-dwb_critics-devel

Obsoletes: ros-humble-dwb-critics < 1.1.15-1

%description
The dwb_critics package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.15-1
- Update to latest release
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.14-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.13-1
- Update to latest release
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.12-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.9-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.9-1
- update to latest upstream release
* Wed Aug 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.9-1
- update to latest upstream
* Fri Jun 30 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.8-1
- update to latest upstream release
* Mon Apr 10 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.6-1
- update to latest upsteam
