# Meta Package
Name:           ros-humble-rqt-reconfigure
Version:        1.1.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_reconfigure
Summary:        Meta package for ros2-humble-rqt_reconfigure and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_reconfigure
Requires:       ros2-humble-rqt_reconfigure-devel

Obsoletes: ros-humble-rqt-reconfigure < 1.1.2-1

%description
This rqt plugin provides a way to view and edit parameters on nodes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.2-1
- update to latest upstream
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.1-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.1-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.5.5-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.1-1
- Initial humble build
