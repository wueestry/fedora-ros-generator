# Meta Package
Name:           ros-jazzy-joint-state-broadcaster
Version:        4.7.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-joint_state_broadcaster and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-joint_state_broadcaster
Requires:       ros2-jazzy-joint_state_broadcaster-devel

Obsoletes: ros-jazzy-joint-state-broadcaster < 4.7.0-1

%description
Broadcaster to publish joint state

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.7.0-1
- Update to latest release
