# Meta Package
Name:           ros-iron-geographic-msgs
Version:        1.0.6
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-geographic_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-geographic_msgs
Requires:       ros2-iron-geographic_msgs-devel

Obsoletes: ros-iron-geographic-msgs < 1.0.6-1

%description
ROS messages for Geographic Information Systems.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.6-1
- Update to latest release
