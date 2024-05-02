# Meta Package
Name:           ros-jazzy-rqt-gui
Version:        1.6.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_gui
Summary:        Meta package for ros2-jazzy-rqt_gui and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_gui
Requires:       ros2-jazzy-rqt_gui-devel

Obsoletes: ros-jazzy-rqt-gui < 1.6.0-1

%description
rqt_gui provides the main to start an instance of the ROS integrated
graphical user interface provided by qt_gui.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.6.0-1
- Update to latest release
