# Meta Package
Name:           ros-humble-rqt-py-console
Version:        1.0.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_py_console
Summary:        Meta package for ros2-humble-rqt_py_console and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_py_console
Requires:       ros2-humble-rqt_py_console-devel

Obsoletes: ros-humble-rqt-py-console < 1.0.2-1

%description
rqt_py_console is a Python GUI plugin providing an interactive Python
console.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.10-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- Initial humble build
