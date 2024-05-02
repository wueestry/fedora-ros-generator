# Meta Package
Name:           ros-iron-webots-ros2-msgs
Version:        2023.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-iron-webots_ros2_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-webots_ros2_msgs
Requires:       ros2-iron-webots_ros2_msgs-devel

Obsoletes: ros-iron-webots-ros2-msgs < 2023.1.2-1

%description
Services and Messages of the webots_ros2 packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2023.1.2-1
- Update to latest release
