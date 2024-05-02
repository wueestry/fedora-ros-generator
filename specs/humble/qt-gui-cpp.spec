# Meta Package
Name:           ros-humble-qt-gui-cpp
Version:        2.2.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_gui_cpp
Summary:        Meta package for ros2-humble-qt_gui_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-qt_gui_cpp
Requires:       ros2-humble-qt_gui_cpp-devel

Obsoletes: ros-humble-qt-gui-cpp < 2.2.3-1

%description
qt_gui_cpp provides the foundation for C++-bindings for qt_gui and
creates bindings for every generator available. At least one specific
binding must be available in order to use C++-plugins.

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
