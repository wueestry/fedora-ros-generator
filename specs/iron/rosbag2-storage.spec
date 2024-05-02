# Meta Package
Name:           ros-iron-rosbag2-storage
Version:        0.22.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rosbag2_storage and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rosbag2_storage
Requires:       ros2-iron-rosbag2_storage-devel

Obsoletes: ros-iron-rosbag2-storage < 0.22.6-1

%description
ROS2 independent storage format to store serialized ROS2 messages

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.22.6-1
- Update to latest release
