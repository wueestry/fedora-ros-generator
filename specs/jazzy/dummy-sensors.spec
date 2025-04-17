# Meta Package
Name:           ros-jazzy-dummy-sensors
Version:        0.33.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-dummy_sensors and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-dummy_sensors
Requires:       ros2-jazzy-dummy_sensors-devel

Obsoletes: ros-jazzy-dummy-sensors < 0.33.5-1

%description
dummy sensor nodes

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.5-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.2-1
- Update to latest release
