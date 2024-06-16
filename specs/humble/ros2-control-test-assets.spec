# Meta Package
Name:           ros-humble-ros2-control-test-assets
Version:        2.41.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ros2_control_test_assets and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ros2_control_test_assets
Requires:       ros2-humble-ros2_control_test_assets-devel

Obsoletes: ros-humble-ros2-control-test-assets < 2.41.0-1

%description
The package provides shared test resources for ros2_control stack

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.41.0-1
- Update to latest release
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.40.0-1
- update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.39.1-1
- Update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.35.1-1
- update to latest upstream
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.33.0-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.30.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.30.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.30.0-1
- update to latest upstream release
* Fri Aug 11 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.29.0-1
- update to latest upstream
* Sat Jul 01 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.28.0-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.25.1-1
- update to latest release
