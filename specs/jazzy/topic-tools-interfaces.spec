# Meta Package
Name:           ros-jazzy-topic-tools-interfaces
Version:        1.3.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-topic_tools_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-topic_tools_interfaces
Requires:       ros2-jazzy-topic_tools_interfaces-devel

Obsoletes: ros-jazzy-topic-tools-interfaces < 1.3.3-1

%description
topic_tools_interfaces contains messages and services for topic_tools

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
