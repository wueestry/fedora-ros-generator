# Meta Package
Name:           ros-humble-ament-cpplint
Version:        0.12.11
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ament_cpplint and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ament_cpplint
Requires:       ros2-humble-ament_cpplint-devel

Obsoletes: ros-humble-ament-cpplint < 0.12.11-1

%description
The ability to check code against the Google style conventions using
cpplint and generate xUnit test result files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.11-1
- Update to latest release
* Mon Feb 12 2024 Tarik Viehmann - humble.0.12.10-1
- update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.9-1
- update to latest upstream
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.8-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.7-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.7-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.7-1
- update to latest release
* Mon Jun 19 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.6-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.5-1
- Initial humble build
