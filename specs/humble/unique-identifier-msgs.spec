# Meta Package
Name:           ros-humble-unique-identifier-msgs
Version:        2.2.1
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-unique_identifier_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-unique_identifier_msgs
Requires:       ros2-humble-unique_identifier_msgs-devel

Obsoletes: ros-humble-unique-identifier-msgs < 2.2.1-1

%description
ROS messages for universally unique identifiers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.1-1
- Initial humble build
