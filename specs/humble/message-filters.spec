# Meta Package
Name:           ros-humble-message-filters
Version:        4.3.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-message_filters and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-message_filters
Requires:       ros2-humble-message_filters-devel

Obsoletes: ros-humble-message-filters < 4.3.4-1

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
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.3.4-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.3.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.3.3-1
- update to latest upstream release
* Mon Jun 19 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.3.3-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.3.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.16.0-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.3.2-1
- Initial humble build
