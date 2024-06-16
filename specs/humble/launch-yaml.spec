# Meta Package
Name:           ros-humble-launch-yaml
Version:        1.0.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-launch_yaml and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-launch_yaml
Requires:       ros2-humble-launch_yaml-devel

Obsoletes: ros-humble-launch-yaml < 1.0.6-1

%description
YAML frontend for the launch package.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.6-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.5-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.4-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.4-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.4-1
- Initial humble build
