# Meta Package
Name:           ros-humble-tf2
Version:        0.25.7
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/tf2
Summary:        Meta package for ros2-humble-tf2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tf2
Requires:       ros2-humble-tf2-devel

Obsoletes: ros-humble-tf2 < 0.25.7-1

%description
tf2 is the second generation of the transform library, which lets the
user keep track of multiple coordinate frames over time. tf2 maintains
the relationship between coordinate frames in a tree structure
buffered in time, and lets the user transform points, vectors, etc
between any two coordinate frames at any desired point in time.

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
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.4-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.3-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.3-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.7.6-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.25.2-1
- Initial humble build
