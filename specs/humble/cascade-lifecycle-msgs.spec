# Meta Package
Name:           ros-humble-cascade-lifecycle-msgs
Version:        1.1.0
Release:        1%{?dist}
License:        Apache License, Version 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-cascade_lifecycle_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-cascade_lifecycle_msgs
Requires:       ros2-humble-cascade_lifecycle_msgs-devel

Obsoletes: ros-humble-cascade-lifecycle-msgs < 1.1.0-1

%description
Messages for rclcpp_cascade_lifecycle package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.0-1
- Update to latest release
* Thu Nov 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest release
* Thu Apr 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest release
