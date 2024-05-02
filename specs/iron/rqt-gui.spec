# Meta Package
Name:           ros-iron-rqt-gui
Version:        1.3.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_gui
Summary:        Meta package for ros2-iron-rqt_gui and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_gui
Requires:       ros2-iron-rqt_gui-devel

Obsoletes: ros-iron-rqt-gui < 1.3.4-1

%description
rqt_gui provides the main to start an instance of the ROS integrated
graphical user interface provided by qt_gui.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.3.4-1
- Update to latest release
