# Meta Package
Name:           ros-humble-qt-dotgraph
Version:        2.2.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_dotgraph
Summary:        Meta package for ros2-humble-qt_dotgraph and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-qt_dotgraph
Requires:       ros2-humble-qt_dotgraph-devel

Obsoletes: ros-humble-qt-dotgraph < 2.2.3-1

%description
qt_dotgraph provides helpers to work with dot graphs.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.3-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.2-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.2-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.2-1
- Initial humble build
