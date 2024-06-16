# Meta Package
Name:           ros-humble-geometry2
Version:        0.25.7
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/geometry2
Summary:        Meta package for ros2-humble-geometry2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-geometry2
Requires:       ros2-humble-geometry2-devel

Obsoletes: ros-humble-geometry2 < 0.25.7-1

%description
A metapackage to bring in the default packages second generation
Transform Library in ros, tf2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.7-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.6-1
- Update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.5-1
- update to latest upstream
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.4-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.3-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.3-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.2-1
- Initial humble build
