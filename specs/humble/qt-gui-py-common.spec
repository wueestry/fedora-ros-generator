# Meta Package
Name:           ros-humble-qt-gui-py-common
Version:        2.2.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_gui_py_common
Summary:        Meta package for ros2-humble-qt_gui_py_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-qt_gui_py_common
Requires:       ros2-humble-qt_gui_py_common-devel

Obsoletes: ros-humble-qt-gui-py-common < 2.2.3-1

%description
qt_gui_py_common provides common functionality for GUI plugins written
in Python.

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
