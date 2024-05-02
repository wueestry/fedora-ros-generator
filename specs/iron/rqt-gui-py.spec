# Meta Package
Name:           ros-iron-rqt-gui-py
Version:        1.3.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_gui_py
Summary:        Meta package for ros2-iron-rqt_gui_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_gui_py
Requires:       ros2-iron-rqt_gui_py-devel

Obsoletes: ros-iron-rqt-gui-py < 1.3.4-1

%description
rqt_gui_py enables GUI plugins to use the Python client library for
ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.3.4-1
- Update to latest release
