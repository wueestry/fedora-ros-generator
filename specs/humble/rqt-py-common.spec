# Meta Package
Name:           ros-humble-rqt-py-common
Version:        1.1.7
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_py_common
Summary:        Meta package for ros2-humble-rqt_py_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_py_common
Requires:       ros2-humble-rqt_py_common-devel

Obsoletes: ros-humble-rqt-py-common < 1.1.7-1

%description
rqt_py_common provides common functionality for rqt plugins written in
Python. Despite no plugin is provided, this package is part of the
rqt_common_plugins repository to keep refactoring generic
functionality from these common plugins into this package as easy as
possible. Functionality included in this package should cover generic
ROS concepts and should not introduce any special dependencies beside
"ros_base".

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
