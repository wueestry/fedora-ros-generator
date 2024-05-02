# Meta Package
Name:           ros-jazzy-rqt-graph
Version:        1.5.3
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_graph
Summary:        Meta package for ros2-jazzy-rqt_graph and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_graph
Requires:       ros2-jazzy-rqt_graph-devel

Obsoletes: ros-jazzy-rqt-graph < 1.5.3-1

%description
rqt_graph provides a GUI plugin for visualizing the ROS computation
graph.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.5.3-1
- Update to latest release
