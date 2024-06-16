# Meta Package
Name:           ros-jazzy-turtlesim
Version:        1.8.3
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/turtlesim
Summary:        Meta package for ros2-jazzy-turtlesim and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-turtlesim
Requires:       ros2-jazzy-turtlesim-devel

Obsoletes: ros-jazzy-turtlesim < 1.8.3-1

%description
turtlesim is a tool made for teaching ROS and ROS packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.8.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.8.2-1
- Update to latest release
