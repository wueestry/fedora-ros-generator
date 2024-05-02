# Meta Package
Name:           ros-iron-rqt-action
Version:        2.1.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_action
Summary:        Meta package for ros2-iron-rqt_action and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_action
Requires:       ros2-iron-rqt_action-devel

Obsoletes: ros-iron-rqt-action < 2.1.2-1

%description
rqt_action provides a feature to introspect all available ROS action
types.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.1.2-1
- Update to latest release
