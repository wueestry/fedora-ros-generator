# Meta Package
Name:           ros-jazzy-gps-msgs
Version:        2.0.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/gps_common
Summary:        Meta package for ros2-jazzy-gps_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gps_msgs
Requires:       ros2-jazzy-gps_msgs-devel

Obsoletes: ros-jazzy-gps-msgs < 2.0.3-1

%description
GPS messages for use in GPS drivers

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.3-1
- Update to latest release
