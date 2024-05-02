# Meta Package
Name:           ros-jazzy-webots-ros2-epuck
Version:        2023.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-jazzy-webots_ros2_epuck and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-webots_ros2_epuck
Requires:       ros2-jazzy-webots_ros2_epuck-devel

Obsoletes: ros-jazzy-webots-ros2-epuck < 2023.1.2-1

%description
E-puck2 driver for Webots simulated robot

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2023.1.2-1
- Update to latest release
