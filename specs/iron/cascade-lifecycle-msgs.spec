# Meta Package
Name:           ros-iron-cascade-lifecycle-msgs
Version:        1.0.5
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-cascade_lifecycle_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-cascade_lifecycle_msgs
Requires:       ros2-iron-cascade_lifecycle_msgs-devel

Obsoletes: ros-iron-cascade-lifecycle-msgs < 1.0.5-1

%description
Messages for rclcpp_cascade_lifecycle package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.5-1
- Update to latest release
