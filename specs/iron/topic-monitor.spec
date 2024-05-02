# Meta Package
Name:           ros-iron-topic-monitor
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-topic_monitor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-topic_monitor
Requires:       ros2-iron-topic_monitor-devel

Obsoletes: ros-iron-topic-monitor < 0.27.1-1

%description
Package containing tools for monitoring ROS 2 topics.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
