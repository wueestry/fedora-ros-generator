# Meta Package
Name:           ros-humble-turtlesim
Version:        1.4.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/turtlesim
Summary:        Meta package for ros2-humble-turtlesim and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-turtlesim
Requires:       ros2-humble-turtlesim-devel

Obsoletes: ros-humble-turtlesim < 1.4.2-1

%description
turtlesim is a tool made for teaching ROS and ROS packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.2-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.2-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.10.2-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.2-1
- Initial humble build
