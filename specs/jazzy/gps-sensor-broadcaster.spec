# Meta Package
Name:           ros-jazzy-gps-sensor-broadcaster
Version:        4.23.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-gps_sensor_broadcaster and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gps_sensor_broadcaster
Requires:       ros2-jazzy-gps_sensor_broadcaster-devel

Obsoletes: ros-jazzy-gps-sensor-broadcaster < 4.23.0-1

%description
Controller to publish readings of GPS sensors.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sun Apr 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.23.0-1
- Update to latest release
