# Meta Package
Name:           ros-humble-rqt-action
Version:        2.0.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_action
Summary:        Meta package for ros2-humble-rqt_action and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_action
Requires:       ros2-humble-rqt_action-devel

Obsoletes: ros-humble-rqt-action < 2.0.1-1

%description
rqt_action provides a feature to introspect all available ROS action
types. By utilizing rqt_msg, the output format is unified with it and
rqt_srv. Note that the actions shown on this plugin is the ones that
are stored on your machine, not on the ROS core your rqt instance
connects to.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.1-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.1-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.9-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.1-1
- Initial humble build
