# Meta Package
Name:           ros-humble-rqt-topic
Version:        1.5.0
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_topic
Summary:        Meta package for ros2-humble-rqt_topic and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_topic
Requires:       ros2-humble-rqt_topic-devel

Obsoletes: ros-humble-rqt-topic < 1.5.0-1

%description
rqt_topic provides a GUI plugin for displaying debug information about
ROS topics including publishers, subscribers, publishing rate, and ROS
Messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.13-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.0-1
- Initial humble build
