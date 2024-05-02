# Meta Package
Name:           ros-jazzy-unique-identifier-msgs
Version:        2.5.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-unique_identifier_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-unique_identifier_msgs
Requires:       ros2-jazzy-unique_identifier_msgs-devel

Obsoletes: ros-jazzy-unique-identifier-msgs < 2.5.0-1

%description
ROS messages for universally unique identifiers.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.0-1
- Update to latest release
