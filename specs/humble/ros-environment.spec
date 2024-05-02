# Meta Package
Name:           ros-humble-ros-environment
Version:        3.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ros_environment and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ros_environment
Requires:       ros2-humble-ros_environment-devel

Obsoletes: ros-humble-ros-environment < 3.2.2-1

%description
The package provides the environment variables `ROS_VERSION` and
`ROS_DISTRO`.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.2-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.3.2-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.2-1
- Initial humble build
