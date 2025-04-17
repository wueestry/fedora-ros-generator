# Meta Package
Name:           ros-jazzy-cascade-lifecycle-msgs
Version:        2.0.0
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-cascade_lifecycle_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-cascade_lifecycle_msgs
Requires:       ros2-jazzy-cascade_lifecycle_msgs-devel

Obsoletes: ros-jazzy-cascade-lifecycle-msgs < 2.0.0-1

%description
Messages for rclcpp_cascade_lifecycle package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.0-1
- Update to latest release
