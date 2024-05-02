# Meta Package
Name:           ros-iron-gazebo-plugins
Version:        3.7.0
Release:        1%{?dist}
License:        BSD, Apache 2.0
URL:            http://gazebosim.org/tutorials?cat=connect_ros
Summary:        Meta package for ros2-iron-gazebo_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-gazebo_plugins
Requires:       ros2-iron-gazebo_plugins-devel

Obsoletes: ros-iron-gazebo-plugins < 3.7.0-1

%description
Robot-independent Gazebo plugins for sensors, motors and dynamic
reconfigurable components.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.7.0-1
- Update to latest release
