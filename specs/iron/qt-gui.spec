# Meta Package
Name:           ros-iron-qt-gui
Version:        2.4.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_gui
Summary:        Meta package for ros2-iron-qt_gui and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-qt_gui
Requires:       ros2-iron-qt_gui-devel

Obsoletes: ros-iron-qt-gui < 2.4.3-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.4.3-1
- Update to latest release
