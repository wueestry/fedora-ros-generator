# Meta Package
Name:           ros-jazzy-srdfdom
Version:        2.0.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/srdfdom
Summary:        Meta package for ros2-jazzy-srdfdom and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-srdfdom
Requires:       ros2-jazzy-srdfdom-devel

Obsoletes: ros-jazzy-srdfdom < 2.0.4-1

%description
Parser for Semantic Robot Description Format (SRDF).

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.4-1
- Update to latest release
