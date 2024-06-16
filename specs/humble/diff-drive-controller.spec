# Meta Package
Name:           ros-humble-diff-drive-controller
Version:        2.35.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-diff_drive_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-diff_drive_controller
Requires:       ros2-humble-diff_drive_controller-devel

Obsoletes: ros-humble-diff-drive-controller < 2.35.0-1

%description
Controller for a differential drive mobile base.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.35.0-1
- Update to latest release
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.34.0-1
- Update to latest release
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.33.0-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.32.0-1
- Update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.28.0-1
- update to latest upstream
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.26.0-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.24.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.24.0-1
- update to latest upstream release
* Fri Aug 11 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.24.0-1
- update to latest upstream
* Sat Jul 01 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.23.0-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.17.3-1
- update to latest release
