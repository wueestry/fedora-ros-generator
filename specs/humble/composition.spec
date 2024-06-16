# Meta Package
Name:           ros-humble-composition
Version:        0.20.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-composition and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-composition
Requires:       ros2-humble-composition-devel

Obsoletes: ros-humble-composition < 0.20.4-1

%description
Examples for composing multiple nodes in a single process.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.4-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- Initial humble build
