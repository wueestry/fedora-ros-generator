# Meta Package
Name:           ros-jazzy-launch-ros
Version:        0.26.7
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-launch_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-launch_ros
Requires:       ros2-jazzy-launch_ros-devel

Obsoletes: ros-jazzy-launch-ros < 0.26.7-1

%description
ROS specific extensions to the launch tool.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.7-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.6-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.5-1
- Update to latest release
