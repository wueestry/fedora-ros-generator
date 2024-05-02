# Meta Package
Name:           ros-iron-rqt-topic
Version:        1.6.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_topic
Summary:        Meta package for ros2-iron-rqt_topic and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_topic
Requires:       ros2-iron-rqt_topic-devel

Obsoletes: ros-iron-rqt-topic < 1.6.1-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.1-1
- Update to latest release
