# Meta Package
Name:           ros-humble-launch-ros
Version:        0.19.7
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-launch_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-launch_ros
Requires:       ros2-humble-launch_ros-devel

Obsoletes: ros-humble-launch-ros < 0.19.7-1

%description
ROS specific extensions to the launch tool.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 12 2024 Tarik Viehmann - humble.0.19.7-1
- update to latest release
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.6-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.5-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.5-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.19.4-1
- Initial humble build
