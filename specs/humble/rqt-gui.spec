# Meta Package
Name:           ros-humble-rqt-gui
Version:        1.1.7
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_gui
Summary:        Meta package for ros2-humble-rqt_gui and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_gui
Requires:       ros2-humble-rqt_gui-devel

Obsoletes: ros-humble-rqt-gui < 1.1.7-1

%description
rqt_gui provides the main to start an instance of the ROS integrated
graphical user interface provided by qt_gui.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.7-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.5-1
- update to latest upstream release
* Thu Jun 29 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.5-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.5.3-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- Initial humble build
