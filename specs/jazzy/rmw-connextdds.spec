# Meta Package
Name:           ros-jazzy-rmw-connextdds
Version:        0.22.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rmw_connextdds and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rmw_connextdds
Requires:       ros2-jazzy-rmw_connextdds-devel

Obsoletes: ros-jazzy-rmw-connextdds < 0.22.0-1

%description
A ROS 2 RMW implementation built with RTI Connext DDS Professional.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.22.0-1
- Update to latest release
