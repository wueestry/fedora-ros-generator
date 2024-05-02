# Meta Package
Name:           ros-humble-gripper-controllers
Version:        2.34.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-gripper_controllers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-gripper_controllers
Requires:       ros2-humble-gripper_controllers-devel

Obsoletes: ros-humble-gripper-controllers < 2.34.0-1

%description
The gripper_controllers package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.34.0-1
- Update to latest release
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.33.0-1
- update to latest release
