# Meta Package
Name:           ros-jazzy-qt-gui
Version:        2.7.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_gui
Summary:        Meta package for ros2-jazzy-qt_gui and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-qt_gui
Requires:       ros2-jazzy-qt_gui-devel

Obsoletes: ros-jazzy-qt-gui < 2.7.4-1

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
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.7.4-1
- Update to latest release
