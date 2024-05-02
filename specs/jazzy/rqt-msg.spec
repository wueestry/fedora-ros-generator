# Meta Package
Name:           ros-jazzy-rqt-msg
Version:        1.5.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_msg
Summary:        Meta package for ros2-jazzy-rqt_msg and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_msg
Requires:       ros2-jazzy-rqt_msg-devel

Obsoletes: ros-jazzy-rqt-msg < 1.5.1-1

%description
A Python GUI plugin for introspecting available ROS message types.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.5.1-1
- Update to latest release
