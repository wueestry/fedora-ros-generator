# Meta Package
Name:           ros-jazzy-geographic-msgs
Version:        1.0.6
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-geographic_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-geographic_msgs
Requires:       ros2-jazzy-geographic_msgs-devel

Obsoletes: ros-jazzy-geographic-msgs < 1.0.6-1

%description
ROS messages for Geographic Information Systems.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.6-1
- Update to latest release
