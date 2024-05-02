# Meta Package
Name:           ros-iron-force-torque-sensor-broadcaster
Version:        3.22.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-force_torque_sensor_broadcaster and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-force_torque_sensor_broadcaster
Requires:       ros2-iron-force_torque_sensor_broadcaster-devel

Obsoletes: ros-iron-force-torque-sensor-broadcaster < 3.22.0-1

%description
Controller to publish state of force-torque sensors.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.22.0-1
- Update to latest release
