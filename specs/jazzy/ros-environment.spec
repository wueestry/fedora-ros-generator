# Meta Package
Name:           ros-jazzy-ros-environment
Version:        4.2.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ros_environment and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ros_environment
Requires:       ros2-jazzy-ros_environment-devel

Obsoletes: ros-jazzy-ros-environment < 4.2.1-1

%description
The package provides the environment variables `ROS_VERSION` and
`ROS_DISTRO`.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.2.1-1
- Update to latest release
