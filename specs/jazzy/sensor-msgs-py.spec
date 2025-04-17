# Meta Package
Name:           ros-jazzy-sensor-msgs-py
Version:        5.3.6
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-sensor_msgs_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-sensor_msgs_py
Requires:       ros2-jazzy-sensor_msgs_py-devel

Obsoletes: ros-jazzy-sensor-msgs-py < 5.3.6-1

%description
A package for easy creation and reading of PointCloud2 messages in
Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.6-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.5-1
- Update to latest release
