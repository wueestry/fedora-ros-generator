# Meta Package
Name:           ros-iron-joint-state-publisher
Version:        2.4.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/joint_state_publisher
Summary:        Meta package for ros2-iron-joint_state_publisher and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-joint_state_publisher
Requires:       ros2-iron-joint_state_publisher-devel

Obsoletes: ros-iron-joint-state-publisher < 2.4.0-1

%description
This package contains a tool for setting and publishing joint state
values for a given URDF.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.4.0-1
- Update to latest release
