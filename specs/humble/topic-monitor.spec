# Meta Package
Name:           ros-humble-topic-monitor
Version:        0.20.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-topic_monitor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-topic_monitor
Requires:       ros2-humble-topic_monitor-devel

Obsoletes: ros-humble-topic-monitor < 0.20.4-1

%description
Package containing tools for monitoring ROS 2 topics.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.4-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- Initial humble build
