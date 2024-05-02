# Meta Package
Name:           ros-jazzy-rosidl-cli
Version:        4.6.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rosidl_cli and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rosidl_cli
Requires:       ros2-jazzy-rosidl_cli-devel

Obsoletes: ros-jazzy-rosidl-cli < 4.6.1-1

%description
Command line tools for ROS interface generation.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.1-1
- Update to latest release
