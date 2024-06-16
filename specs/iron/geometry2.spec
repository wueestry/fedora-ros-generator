# Meta Package
Name:           ros-iron-geometry2
Version:        0.31.7
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/geometry2
Summary:        Meta package for ros2-iron-geometry2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-geometry2
Requires:       ros2-iron-geometry2-devel

Obsoletes: ros-iron-geometry2 < 0.31.7-1

%description
A metapackage to bring in the default packages second generation
Transform Library in ros, tf2.

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
