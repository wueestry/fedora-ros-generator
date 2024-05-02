# Meta Package
Name:           ros-iron-rqt-common-plugins
Version:        1.2.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_common_plugins
Summary:        Meta package for ros2-iron-rqt_common_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_common_plugins
Requires:       ros2-iron-rqt_common_plugins-devel

Obsoletes: ros-iron-rqt-common-plugins < 1.2.0-1

%description
rqt_common_plugins metapackage provides ROS backend graphical tools
suite that can be used on/off of robot runtime.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.0-1
- Update to latest release
