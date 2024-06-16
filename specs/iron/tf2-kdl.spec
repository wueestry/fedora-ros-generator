# Meta Package
Name:           ros-iron-tf2-kdl
Version:        0.31.7
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/tf2
Summary:        Meta package for ros2-iron-tf2_kdl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tf2_kdl
Requires:       ros2-iron-tf2_kdl-devel

Obsoletes: ros-iron-tf2-kdl < 0.31.7-1

%description
KDL binding for tf2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.7-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.6-1
- Update to latest release
