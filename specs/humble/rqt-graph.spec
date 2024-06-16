# Meta Package
Name:           ros-humble-rqt-graph
Version:        1.3.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_graph
Summary:        Meta package for ros2-humble-rqt_graph and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_graph
Requires:       ros2-humble-rqt_graph-devel

Obsoletes: ros-humble-rqt-graph < 1.3.1-1

%description
rqt_graph provides a GUI plugin for visualizing the ROS computation
graph.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.1-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.14-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.3.0-1
- Initial humble build
