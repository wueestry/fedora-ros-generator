# Meta Package
Name:           ros-iron-range-sensor-broadcaster
Version:        3.24.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-range_sensor_broadcaster and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-range_sensor_broadcaster
Requires:       ros2-iron-range_sensor_broadcaster-devel

Obsoletes: ros-iron-range-sensor-broadcaster < 3.24.0-1

%description
Controller to publish readings of Range sensors.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.22.0-1
- Update to latest release
