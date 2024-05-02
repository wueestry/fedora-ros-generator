# Meta Package
Name:           ros-humble-graph-msgs
Version:        0.2.0
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/davetcoleman/graph_msgs
Summary:        Meta package for ros2-humble-graph_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-graph_msgs
Requires:       ros2-humble-graph_msgs-devel

Obsoletes: ros-humble-graph-msgs < 0.2.0-1

%description
ROS messages for publishing graphs of different data types

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Feb 22 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.0-1
- Update to latest release
