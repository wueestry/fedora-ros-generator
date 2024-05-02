# Meta Package
Name:           ros-humble-rqt-gui-py
Version:        1.1.7
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_gui_py
Summary:        Meta package for ros2-humble-rqt_gui_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_gui_py
Requires:       ros2-humble-rqt_gui_py-devel

Obsoletes: ros-humble-rqt-gui-py < 1.1.7-1

%description
rqt_gui_py enables GUI plugins to use the Python client library for
ROS.

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
