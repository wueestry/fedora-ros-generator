# Meta Package
Name:           ros-jazzy-rqt-bag-plugins
Version:        1.5.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_bag
Summary:        Meta package for ros2-jazzy-rqt_bag_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_bag_plugins
Requires:       ros2-jazzy-rqt_bag_plugins-devel

Obsoletes: ros-jazzy-rqt-bag-plugins < 1.5.2-1

%description
rqt_bag provides a GUI plugin for displaying and replaying ROS bag
files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.5.2-1
- Update to latest release
