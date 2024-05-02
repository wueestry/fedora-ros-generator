# Meta Package
Name:           ros-iron-interactive-markers
Version:        2.4.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-interactive_markers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-interactive_markers
Requires:       ros2-iron-interactive_markers-devel

Obsoletes: ros-iron-interactive-markers < 2.4.0-1

%description
3D interactive marker communication library for RViz and similar
tools.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.4.0-1
- Update to latest release
