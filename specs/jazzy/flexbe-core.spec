# Meta Package
Name:           ros-jazzy-flexbe-core
Version:        3.0.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/flexbe_core
Summary:        Meta package for ros2-jazzy-flexbe_core and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-flexbe_core
Requires:       ros2-jazzy-flexbe_core-devel

Obsoletes: ros-jazzy-flexbe-core < 3.0.3-1

%description
flexbe_core provides the core components for the FlexBE behavior
engine.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.3-1
- Update to latest release
