# Meta Package
Name:           ros-jazzy-rqt-gui-py
Version:        1.6.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_gui_py
Summary:        Meta package for ros2-jazzy-rqt_gui_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_gui_py
Requires:       ros2-jazzy-rqt_gui_py-devel

Obsoletes: ros-jazzy-rqt-gui-py < 1.6.0-1

%description
rqt_gui_py enables GUI plugins to use the Python client library for
ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.6.0-1
- Update to latest release
