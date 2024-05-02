# Meta Package
Name:           ros-humble-sros2
Version:        0.10.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-sros2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-sros2
Requires:       ros2-humble-sros2-devel

Obsoletes: ros-humble-sros2 < 0.10.4-1

%description
Command line tools for managing SROS2 keys

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.4-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.4-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.4-1
- Initial humble build
