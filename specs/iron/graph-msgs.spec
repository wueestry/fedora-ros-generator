# Meta Package
Name:           ros-iron-graph-msgs
Version:        0.2.0
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/davetcoleman/graph_msgs
Summary:        Meta package for ros2-iron-graph_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-graph_msgs
Requires:       ros2-iron-graph_msgs-devel

Obsoletes: ros-iron-graph-msgs < 0.2.0-1

%description
ROS messages for publishing graphs of different data types

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.2.0-1
- Update to latest release
