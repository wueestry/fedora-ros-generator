# Meta Package
Name:           ros-humble-joint-state-broadcaster
Version:        2.37.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-joint_state_broadcaster and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-joint_state_broadcaster
Requires:       ros2-humble-joint_state_broadcaster-devel

Obsoletes: ros-humble-joint-state-broadcaster < 2.37.0-1

%description
Broadcaster to publish joint state

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.37.0-1
- Update to latest release
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
