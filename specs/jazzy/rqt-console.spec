# Meta Package
Name:           ros-jazzy-rqt-console
Version:        2.2.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_console
Summary:        Meta package for ros2-jazzy-rqt_console and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_console
Requires:       ros2-jazzy-rqt_console-devel

Obsoletes: ros-jazzy-rqt-console < 2.2.1-1

%description
rqt_console provides a GUI plugin for displaying and filtering ROS
messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.2.1-1
- Update to latest release
