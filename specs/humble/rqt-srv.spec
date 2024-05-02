# Meta Package
Name:           ros-humble-rqt-srv
Version:        1.0.3
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_srv
Summary:        Meta package for ros2-humble-rqt_srv and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_srv
Requires:       ros2-humble-rqt_srv-devel

Obsoletes: ros-humble-rqt-srv < 1.0.3-1

%description
A Python GUI plugin for introspecting available ROS message types.
Note that the srvs available through this plugin is the ones that are
stored on your machine, not on the ROS core your rqt instance connects
to.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.3-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.3-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.9-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.3-1
- Initial humble build
