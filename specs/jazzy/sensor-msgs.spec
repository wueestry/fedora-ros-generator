# Meta Package
Name:           ros-jazzy-sensor-msgs
Version:        5.3.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-sensor_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-sensor_msgs
Requires:       ros2-jazzy-sensor_msgs-devel

Obsoletes: ros-jazzy-sensor-msgs < 5.3.5-1

%description
A package containing some sensor data related message and service
definitions.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.5-1
- Update to latest release
