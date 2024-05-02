# Meta Package
Name:           ros-humble-qt-gui
Version:        2.2.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_gui
Summary:        Meta package for ros2-humble-qt_gui and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-qt_gui
Requires:       ros2-humble-qt_gui-devel

Obsoletes: ros-humble-qt-gui < 2.2.3-1

%description
qt_gui provides the infrastructure for an integrated graphical user
interface based on Qt. It is extensible with Python- and C++-based
plugins (implemented in separate packages) which can contribute
arbitrary widgets. It requires either PyQt or PySide bindings.

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
