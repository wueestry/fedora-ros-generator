# Meta Package
Name:           ros-humble-python-qt-binding
Version:        1.1.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-python_qt_binding and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-python_qt_binding
Requires:       ros2-humble-python_qt_binding-devel

Obsoletes: ros-humble-python-qt-binding < 1.1.2-1

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
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.2-1
- Change from pyside2 to PyQt
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.1-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.1-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.4-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.1-1
- Initial humble build
