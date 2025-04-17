# Meta Package
Name:           ros-jazzy-topic-tools
Version:        1.3.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-topic_tools and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-topic_tools
Requires:       ros2-jazzy-topic_tools-devel

Obsoletes: ros-jazzy-topic-tools < 1.3.3-1

%description
Tools for directing, throttling, selecting, and otherwise messing with
ROS 2 topics at a meta level.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.3-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
