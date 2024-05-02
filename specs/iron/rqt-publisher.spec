# Meta Package
Name:           ros-iron-rqt-publisher
Version:        1.6.3
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_publisher
Summary:        Meta package for ros2-iron-rqt_publisher and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_publisher
Requires:       ros2-iron-rqt_publisher-devel

Obsoletes: ros-iron-rqt-publisher < 1.6.3-1

%description
rqt_publisher provides a GUI plugin for publishing arbitrary messages
with fixed or computed field values.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.3-1
- Update to latest release
