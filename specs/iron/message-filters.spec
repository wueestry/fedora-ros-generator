# Meta Package
Name:           ros-iron-message-filters
Version:        4.7.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-message_filters and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-message_filters
Requires:       ros2-iron-message_filters-devel

Obsoletes: ros-iron-message-filters < 4.7.0-1

%description
A set of ROS2 message filters which take in messages and may output
those messages at a later time, based on the conditions that filter
needs met.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.7.0-1
- Update to latest release
