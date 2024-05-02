# Meta Package
Name:           ros-iron-moveit-msgs
Version:        2.3.0
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-iron-moveit_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_msgs
Requires:       ros2-iron-moveit_msgs-devel

Obsoletes: ros-iron-moveit-msgs < 2.3.0-1

%description
Messages, services and actions used by MoveIt

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.3.0-1
- Update to latest release
