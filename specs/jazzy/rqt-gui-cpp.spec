# Meta Package
Name:           ros-jazzy-rqt-gui-cpp
Version:        1.6.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_gui_cpp
Summary:        Meta package for ros2-jazzy-rqt_gui_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_gui_cpp
Requires:       ros2-jazzy-rqt_gui_cpp-devel

Obsoletes: ros-jazzy-rqt-gui-cpp < 1.6.0-1

%description
rqt_gui_cpp enables GUI plugins to use the C++ client library for ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.6.0-1
- Update to latest release
