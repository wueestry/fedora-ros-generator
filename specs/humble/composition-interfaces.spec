# Meta Package
Name:           ros-humble-composition-interfaces
Version:        1.2.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-composition_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-composition_interfaces
Requires:       ros2-humble-composition_interfaces-devel

Obsoletes: ros-humble-composition-interfaces < 1.2.1-1

%description
A package containing message and service definitions for managing
composable nodes in a container process.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.1-1
- Initial humble build
