# Meta Package
Name:           ros-jazzy-rqt-srv
Version:        1.2.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_srv
Summary:        Meta package for ros2-jazzy-rqt_srv and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_srv
Requires:       ros2-jazzy-rqt_srv-devel

Obsoletes: ros-jazzy-rqt-srv < 1.2.2-1

%description
A Python GUI plugin for introspecting available ROS service types.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.2.2-1
- Update to latest release
