# Meta Package
Name:           ros-iron-joint-state-broadcaster
Version:        3.24.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-joint_state_broadcaster and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-joint_state_broadcaster
Requires:       ros2-iron-joint_state_broadcaster-devel

Obsoletes: ros-iron-joint-state-broadcaster < 3.24.0-1

%description
Broadcaster to publish joint state

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.22.0-1
- Update to latest release
