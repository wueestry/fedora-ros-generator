# Meta Package
Name:           ros-humble-robot-state-publisher
Version:        3.0.3
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-robot_state_publisher and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-robot_state_publisher
Requires:       ros2-humble-robot_state_publisher-devel

Obsoletes: ros-humble-robot-state-publisher < 3.0.3-1

%description
This package take the joint angles of a robot as input, and publishes
the 3D poses of the robot links to tf2, using a kinematic tree model
of the robot.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.3-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.15.2-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.2-1
- Initial humble build
