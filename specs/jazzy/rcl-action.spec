# Meta Package
Name:           ros-jazzy-rcl-action
Version:        9.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcl_action and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcl_action
Requires:       ros2-jazzy-rcl_action-devel

Obsoletes: ros-jazzy-rcl-action < 9.2.2-1

%description
Package containing a C-based ROS action implementation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.2-1
- Update to latest release
