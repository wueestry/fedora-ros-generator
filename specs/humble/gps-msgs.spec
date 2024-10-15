# Meta Package
Name:           ros-humble-gps-msgs
Version:        2.0.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/gps_common
Summary:        Meta package for ros2-humble-gps_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-gps_msgs
Requires:       ros2-humble-gps_msgs-devel

Obsoletes: ros-humble-gps-msgs < 2.0.4-1

%description
GPS messages for use in GPS drivers

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.4-1
- Update to latest release
