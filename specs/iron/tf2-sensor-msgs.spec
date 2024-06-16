# Meta Package
Name:           ros-iron-tf2-sensor-msgs
Version:        0.31.7
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/tf2_ros
Summary:        Meta package for ros2-iron-tf2_sensor_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tf2_sensor_msgs
Requires:       ros2-iron-tf2_sensor_msgs-devel

Obsoletes: ros-iron-tf2-sensor-msgs < 0.31.7-1

%description
Small lib to transform sensor_msgs with tf. Most notably, PointCloud2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.7-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.6-1
- Update to latest release
