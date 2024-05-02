# Meta Package
Name:           ros-iron-rqt-bag-plugins
Version:        1.3.4
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_bag
Summary:        Meta package for ros2-iron-rqt_bag_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_bag_plugins
Requires:       ros2-iron-rqt_bag_plugins-devel

Obsoletes: ros-iron-rqt-bag-plugins < 1.3.4-1

%description
rqt_bag provides a GUI plugin for displaying and replaying ROS bag
files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.3.4-1
- Update to latest release
