# Meta Package
Name:           ros-jazzy-rqt-action
Version:        2.2.0
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_action
Summary:        Meta package for ros2-jazzy-rqt_action and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_action
Requires:       ros2-jazzy-rqt_action-devel

Obsoletes: ros-jazzy-rqt-action < 2.2.0-1

%description
rqt_action provides a feature to introspect all available ROS action
types.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.2.0-1
- Update to latest release
