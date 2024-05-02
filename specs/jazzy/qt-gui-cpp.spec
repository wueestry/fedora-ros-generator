# Meta Package
Name:           ros-jazzy-qt-gui-cpp
Version:        2.7.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_gui_cpp
Summary:        Meta package for ros2-jazzy-qt_gui_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-qt_gui_cpp
Requires:       ros2-jazzy-qt_gui_cpp-devel

Obsoletes: ros-jazzy-qt-gui-cpp < 2.7.4-1

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
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.7.4-1
- Update to latest release
