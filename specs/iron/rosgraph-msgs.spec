# Meta Package
Name:           ros-iron-rosgraph-msgs
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosgraph_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosgraph_msgs
Requires:       ros2-iron-rosgraph_msgs-devel

Obsoletes: ros-iron-rosgraph-msgs < 1.6.0-1

%description
Messages relating to the ROS Computation Graph. These are generally
considered to be low-level messages that end users do not interact
with.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.0-1
- Update to latest release
