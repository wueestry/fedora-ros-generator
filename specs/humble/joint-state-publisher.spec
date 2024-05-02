# Meta Package
Name:           ros-humble-joint-state-publisher
Version:        2.4.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/joint_state_publisher
Summary:        Meta package for ros2-humble-joint_state_publisher and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-joint_state_publisher
Requires:       ros2-humble-joint_state_publisher-devel

Obsoletes: ros-humble-joint-state-publisher < 2.4.0-1

%description
This package contains a tool for setting and publishing joint state
values for a given URDF.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.0-1
- update to latest release
* Fri Aug 11 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.0-1
- update to latest upstream
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.15.1-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.3.0-1
- Initial humble build
