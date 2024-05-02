# Meta Package
Name:           ros-iron-rqt-console
Version:        2.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_console
Summary:        Meta package for ros2-iron-rqt_console and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_console
Requires:       ros2-iron-rqt_console-devel

Obsoletes: ros-iron-rqt-console < 2.1.1-1

%description
rqt_console provides a GUI plugin for displaying and filtering ROS
messages.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.1.1-1
- Update to latest release
