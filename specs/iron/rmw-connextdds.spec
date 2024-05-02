# Meta Package
Name:           ros-iron-rmw-connextdds
Version:        0.14.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rmw_connextdds and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rmw_connextdds
Requires:       ros2-iron-rmw_connextdds-devel

Obsoletes: ros-iron-rmw-connextdds < 0.14.1-1

%description
A ROS 2 RMW implementation built with RTI Connext DDS Professional.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.14.1-1
- Update to latest release
