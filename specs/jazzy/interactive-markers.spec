# Meta Package
Name:           ros-jazzy-interactive-markers
Version:        2.5.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-interactive_markers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-interactive_markers
Requires:       ros2-jazzy-interactive_markers-devel

Obsoletes: ros-jazzy-interactive-markers < 2.5.4-1

%description
3D interactive marker communication library for RViz and similar
tools.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.4-1
- Update to latest release
