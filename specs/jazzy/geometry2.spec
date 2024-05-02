# Meta Package
Name:           ros-jazzy-geometry2
Version:        0.36.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/geometry2
Summary:        Meta package for ros2-jazzy-geometry2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-geometry2
Requires:       ros2-jazzy-geometry2-devel

Obsoletes: ros-jazzy-geometry2 < 0.36.2-1

%description
A metapackage to bring in the default packages second generation
Transform Library in ros, tf2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.2-1
- Update to latest release
