# Meta Package
Name:           ros-humble-geographic-msgs
Version:        1.0.6
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-geographic_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-geographic_msgs
Requires:       ros2-humble-geographic_msgs-devel

Obsoletes: ros-humble-geographic-msgs < 1.0.6-1

%description
ROS messages for Geographic Information Systems.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.6-1
- Update to latest release
* Mon Feb 12 2024 Tarik Viehmann - humble.1.0.5-1
- update to latest release
