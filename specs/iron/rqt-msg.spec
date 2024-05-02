# Meta Package
Name:           ros-iron-rqt-msg
Version:        1.3.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_msg
Summary:        Meta package for ros2-iron-rqt_msg and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_msg
Requires:       ros2-iron-rqt_msg-devel

Obsoletes: ros-iron-rqt-msg < 1.3.1-1

%description
A Python GUI plugin for introspecting available ROS message types.
Note that the msgs available through this plugin is the ones that are
stored on your machine, not on the ROS core your rqt instance connects
to.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.3.1-1
- Update to latest release
