# Meta Package
Name:           ros-jazzy-moveit-msgs
Version:        2.4.0
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_msgs
Requires:       ros2-jazzy-moveit_msgs-devel

Obsoletes: ros-jazzy-moveit-msgs < 2.4.0-1

%description
Messages, services and actions used by MoveIt

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.4.0-1
- Update to latest release
