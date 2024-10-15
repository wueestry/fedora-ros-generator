# Meta Package
Name:           ros-humble-laser-filters
Version:        2.0.7
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-laser_filters and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-laser_filters
Requires:       ros2-humble-laser_filters-devel

Obsoletes: ros-humble-laser-filters < 2.0.7-1

%description
Assorted filters designed to operate on 2D planar laser scanners,
which use the sensor_msgs/LaserScan type.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.7-1
- Update to latest release
