# Meta Package
Name:           ros-iron-rqt-reconfigure
Version:        1.3.4
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_reconfigure
Summary:        Meta package for ros2-iron-rqt_reconfigure and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_reconfigure
Requires:       ros2-iron-rqt_reconfigure-devel

Obsoletes: ros-iron-rqt-reconfigure < 1.3.4-1

%description
This rqt plugin provides a way to view and edit parameters on nodes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.3.4-1
- Update to latest release
