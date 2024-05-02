# Meta Package
Name:           ros-humble-moveit-msgs
Version:        2.2.1
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-humble-moveit_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-moveit_msgs
Requires:       ros2-humble-moveit_msgs-devel

Obsoletes: ros-humble-moveit-msgs < 2.2.1-1

%description
Messages, services and actions used by MoveIt

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.1-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.1-1
- Initial humble build
