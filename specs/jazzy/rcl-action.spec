# Meta Package
Name:           ros-jazzy-rcl-action
Version:        9.2.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcl_action and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcl_action
Requires:       ros2-jazzy-rcl_action-devel

Obsoletes: ros-jazzy-rcl-action < 9.2.5-1

%description
Package containing a C-based ROS action implementation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.5-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.2-1
- Update to latest release
