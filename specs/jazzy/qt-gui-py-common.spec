# Meta Package
Name:           ros-jazzy-qt-gui-py-common
Version:        2.7.5
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_gui_py_common
Summary:        Meta package for ros2-jazzy-qt_gui_py_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-qt_gui_py_common
Requires:       ros2-jazzy-qt_gui_py_common-devel

Obsoletes: ros-jazzy-qt-gui-py-common < 2.7.5-1

%description
qt_gui_py_common provides common functionality for GUI plugins written
in Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.7.5-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.7.4-1
- Update to latest release
