# Meta Package
Name:           ros-iron-rqt-py-console
Version:        1.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_py_console
Summary:        Meta package for ros2-iron-rqt_py_console and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_py_console
Requires:       ros2-iron-rqt_py_console-devel

Obsoletes: ros-iron-rqt-py-console < 1.1.1-1

%description
rqt_py_console is a Python GUI plugin providing an interactive Python
console.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.1.1-1
- Update to latest release
