# Meta Package
Name:           ros-humble-ros2cli-test-interfaces
Version:        0.18.9
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ros2cli_test_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ros2cli_test_interfaces
Requires:       ros2-humble-ros2cli_test_interfaces-devel

Obsoletes: ros-humble-ros2cli-test-interfaces < 0.18.9-1

%description
A package containing interface definitions for testing ros2cli.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.18.9-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.18.7-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.18.7-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.18.7-1
- update to latest upstream
* Thu Jun 29 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.18.6-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.18.5-1
- Initial humble build
