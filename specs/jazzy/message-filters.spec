# Meta Package
Name:           ros-jazzy-message-filters
Version:        4.11.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-message_filters and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-message_filters
Requires:       ros2-jazzy-message_filters-devel

Obsoletes: ros-jazzy-message-filters < 4.11.2-1

%description
A set of ROS 2 message filters which take in messages and may output
those messages at a later time, based on the conditions that filter
needs met.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Aug 01 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.11.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.11.1-1
- Update to latest release
