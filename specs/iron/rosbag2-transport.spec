# Meta Package
Name:           ros-iron-rosbag2-transport
Version:        0.22.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosbag2_transport and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosbag2_transport
Requires:       ros2-iron-rosbag2_transport-devel

Obsoletes: ros-iron-rosbag2-transport < 0.22.6-1

%description
Layer encapsulating ROS middleware to allow rosbag2 to be used with or
without middleware

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest release
