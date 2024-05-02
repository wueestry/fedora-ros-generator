# Meta Package
Name:           ros-iron-rqt-graph
Version:        1.4.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_graph
Summary:        Meta package for ros2-iron-rqt_graph and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_graph
Requires:       ros2-iron-rqt_graph-devel

Obsoletes: ros-iron-rqt-graph < 1.4.2-1

%description
rqt_graph provides a GUI plugin for visualizing the ROS computation
graph.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.4.2-1
- Update to latest release
