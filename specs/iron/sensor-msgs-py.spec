# Meta Package
Name:           ros-iron-sensor-msgs-py
Version:        5.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-sensor_msgs_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-sensor_msgs_py
Requires:       ros2-iron-sensor_msgs_py-devel

Obsoletes: ros-iron-sensor-msgs-py < 5.0.0-1

%description
A package for easy creation and reading of PointCloud2 messages in
Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.5.0.0-1
- Update to latest release
