# Meta Package
Name:           ros-jazzy-rqt-reconfigure
Version:        1.6.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_reconfigure
Summary:        Meta package for ros2-jazzy-rqt_reconfigure and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_reconfigure
Requires:       ros2-jazzy-rqt_reconfigure-devel

Obsoletes: ros-jazzy-rqt-reconfigure < 1.6.2-1

%description
This rqt plugin provides a way to view and edit parameters on nodes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.6.2-1
- Update to latest release
