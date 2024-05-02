# Meta Package
Name:           ros-jazzy-rqt-publisher
Version:        1.7.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_publisher
Summary:        Meta package for ros2-jazzy-rqt_publisher and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_publisher
Requires:       ros2-jazzy-rqt_publisher-devel

Obsoletes: ros-jazzy-rqt-publisher < 1.7.2-1

%description
rqt_publisher provides a GUI plugin for publishing arbitrary messages
with fixed or computed field values.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.7.2-1
- Update to latest release
