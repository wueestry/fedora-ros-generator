# Meta Package
Name:           ros-jazzy-flexbe-onboard
Version:        3.0.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/flexbe_core
Summary:        Meta package for ros2-jazzy-flexbe_onboard and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-flexbe_onboard
Requires:       ros2-jazzy-flexbe_onboard-devel

Obsoletes: ros-jazzy-flexbe-onboard < 3.0.3-1

%description
flexbe_onboard implements the robot-side of the behavior engine from
where all behaviors are started.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.3-1
- Update to latest release
