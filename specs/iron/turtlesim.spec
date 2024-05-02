# Meta Package
Name:           ros-iron-turtlesim
Version:        1.6.1
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/turtlesim
Summary:        Meta package for ros2-iron-turtlesim and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-turtlesim
Requires:       ros2-iron-turtlesim-devel

Obsoletes: ros-iron-turtlesim < 1.6.1-1

%description
turtlesim is a tool made for teaching ROS and ROS packages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.1-1
- Update to latest release
