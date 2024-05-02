# Meta Package
Name:           ros-jazzy-python-qt-binding
Version:        2.2.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-python_qt_binding and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-python_qt_binding
Requires:       ros2-jazzy-python_qt_binding-devel

Obsoletes: ros-jazzy-python-qt-binding < 2.2.0-1

%description
This stack provides Python bindings for Qt. There are two providers:
pyside and pyqt. PySide2 is available under the GPL, LGPL and a
commercial license. PyQt is released under the GPL. Both the bindings
and tools to build bindings are included from each available provider.
For PySide, it is called "Shiboken". For PyQt, this is called "SIP".
Also provided is adapter code to make the user's Python code
independent of which binding provider was actually used which makes it
very easy to switch between these.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.2.0-1
- Update to latest release
