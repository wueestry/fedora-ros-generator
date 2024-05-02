# Meta Package
Name:           ros-humble-joy
Version:        3.3.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-joy and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-joy
Requires:       ros2-humble-joy-devel

Obsoletes: ros-humble-joy < 3.3.0-1

%description
The joy package contains joy_node, a node that interfaces a generic
joystick to ROS 2. This node publishes a "Joy" message, which contains
the current state of each one of the joystick's buttons and axes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.3.0-1
- update to latest upstream
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.0-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.0-1
- Initial humble build
