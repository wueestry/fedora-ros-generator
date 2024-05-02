# Meta Package
Name:           ros-jazzy-rqt-topic
Version:        1.7.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_topic
Summary:        Meta package for ros2-jazzy-rqt_topic and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_topic
Requires:       ros2-jazzy-rqt_topic-devel

Obsoletes: ros-jazzy-rqt-topic < 1.7.2-1

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
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.7.2-1
- Update to latest release
