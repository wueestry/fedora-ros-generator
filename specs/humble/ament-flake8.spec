# Meta Package
Name:           ros-humble-ament-flake8
Version:        0.12.11
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ament_flake8 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ament_flake8
Requires:       ros2-humble-ament_flake8-devel

Obsoletes: ros-humble-ament-flake8 < 0.12.11-1

%description
The ability to check code for style and syntax conventions with
flake8.

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
* Sun Jun 18 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.6-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.5-1
- Initial humble build
