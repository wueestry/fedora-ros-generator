# Meta Package
Name:           ros-humble-cyclonedds
Version:        0.10.4
Release:        1%{?dist}
License:        Eclipse Public License 2.0
URL:            https://projects.eclipse.org/projects/iot.cyclonedds
Summary:        Meta package for ros2-humble-cyclonedds and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-cyclonedds
Requires:       ros2-humble-cyclonedds-devel

Obsoletes: ros-humble-cyclonedds < 0.10.4-1

%description
Eclipse Cyclone DDS is a very performant and robust open-source DDS
implementation. Cyclone DDS is developed completely in the open as an
Eclipse IoT project.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 12 2024 Tarik Viehmann - humble.0.10.4-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.9.1-1
- Initial humble build
