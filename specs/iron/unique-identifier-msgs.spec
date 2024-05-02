# Meta Package
Name:           ros-iron-unique-identifier-msgs
Version:        2.3.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-unique_identifier_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-unique_identifier_msgs
Requires:       ros2-iron-unique_identifier_msgs-devel

Obsoletes: ros-iron-unique-identifier-msgs < 2.3.2-1

%description
ROS messages for universally unique identifiers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.3.2-1
- Update to latest release
