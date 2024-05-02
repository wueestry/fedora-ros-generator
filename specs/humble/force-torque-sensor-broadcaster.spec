# Meta Package
Name:           ros-humble-force-torque-sensor-broadcaster
Version:        2.34.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-force_torque_sensor_broadcaster and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-force_torque_sensor_broadcaster
Requires:       ros2-humble-force_torque_sensor_broadcaster-devel

Obsoletes: ros-humble-force-torque-sensor-broadcaster < 2.34.0-1

%description
Controller to publish state of force-torque sensors.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.34.0-1
- Update to latest release
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.33.0-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.32.0-1
- Update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.28.0-1
- update to latest upstream
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.26.0-1
- update to latest release
