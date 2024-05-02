# Meta Package
Name:           ros-humble-rqt-msg
Version:        1.2.0
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_msg
Summary:        Meta package for ros2-humble-rqt_msg and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_msg
Requires:       ros2-humble-rqt_msg-devel

Obsoletes: ros-humble-rqt-msg < 1.2.0-1

%description
A Python GUI plugin for introspecting available ROS message types.
Note that the msgs available through this plugin is the ones that are
stored on your machine, not on the ROS core your rqt instance connects
to.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.10-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- Initial humble build
